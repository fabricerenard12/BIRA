import multiprocessing
from scipy.stats import trim_mean
import speech_to_text
import numpy as np
from text_viewer import TextViewer
from time import sleep
import utils
import history as history
import detector
import argparse
import torch
import math
import faulthandler
import uart
from enum import Enum

faulthandler.enable()

class Mode(Enum):
    FIX_THRESHOLD = 0
    TRIMMED = 1

def find_angle(coordinated_target_list:np.ndarray, mode: Mode = Mode.FIX_THRESHOLD) -> int:
    x = z = 0
    if mode == Mode.TRIMMED:
        x = trim_mean(coordinated_target_list[:,0], proportiontocut=0.1)
        z = trim_mean(coordinated_target_list[:,2], proportiontocut=0.1)
    elif mode == Mode.FIX_THRESHOLD:
        x = history.get_distance(coordinated_target_list[:,0])
        z = history.get_distance(coordinated_target_list[:,2])
    
    angle_rad = math.atan(x / z)
    angle_deg = math.degrees(angle_rad)
    return angle_deg

def run_test_motors():
    while True:
            try:
                a = input("Enter angle: ")
                b = input("Enter motor ID: ")
                if input("Do you want to enter velocity? (y/N): ").strip().lower() == 'y':
                    c = input("Enter velocity %: ")
                else:
                    c = 80
                uart.send_data_through_UART(int(a), int(b), int(c))
                print("Data sent successfully.\n")
            except ValueError:
                print("Invalid input. Please enter numeric values.\n\n")           

def run_stt():
    def run_text_window(queue: multiprocessing.Queue):
        app = TextViewer(queue)
        app.open()
        
    text_queue = multiprocessing.Queue()
    text_process = multiprocessing.Process(target=run_text_window, args=(text_queue,))
    text_process.start()

    text_queue.put("Je suis BIRA, le bras robotique de HEKA.")
    sleep(3)
    
    while True:
        text_queue.put({"text": "Dis moi quelque chose!", "countdown": 10})
        text = speech_to_text.transcribe_for(10)
        text_queue.put({"text": f"Tu as dis: \n{text}", "countdown": 10})
        sleep(10)

def run_bira_sequence(opt): 
    text = speech_to_text.transcribe_directly()
    print(text)
    label = utils.string_to_label(text)
    print(label)   
    with torch.no_grad():
        coordinate_dict = detector.object_detection(60, opt)

        if label not in coordinate_dict:
            raise ValueError(f"Label {label} not found in coordinate dictionary.")
        else:
            for obj_id, positions in coordinate_dict[label].items():
                angle = find_angle(positions)
                print(f"Angle for object ID {obj_id} with label {label}: {angle}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', type=str, default='../models/yolov8n.pt', help='model.pt path(s)')
    parser.add_argument('--svo', type=str, default=None, help='optional svo file')
    parser.add_argument('--img_size', type=int, default=416, help='inference size (pixels)')
    parser.add_argument('--conf_thres', type=float, default=0.4, help='object confidence threshold')
    parser.add_argument('--stt', action="store_true", help='Run sheech to text app')
    parser.add_argument('--motors', help='Testing motors app')
    opt = parser.parse_args()

    if opt.stt:
        run_stt()
    elif opt.motors:
        run_test_motors()
    else:
        run_bira_sequence(opt)
        
if __name__ == '__main__':
    main()
