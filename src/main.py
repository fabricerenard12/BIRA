from scipy.stats import trim_mean
import speech_to_text
import numpy as np
import algorithm
import outputs.retrieve_data as retrieve_data
import detector
import argparse
import torch
import math
import faulthandler
import UART
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
        x = retrieve_data.get_distance(coordinated_target_list[:,0])
        z = retrieve_data.get_distance(coordinated_target_list[:,2])
    
    angle_rad = math.atan(x / z)
    angle_deg = math.degrees(angle_rad)
    return angle_deg

def main():
    text = speech_to_text.transcribe_directly()
    print(text)
    label = algorithm.string_to_label(text)
    print(label)

    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', type=str, default='../models/yolov8n.pt', help='model.pt path(s)')
    parser.add_argument('--svo', type=str, default=None, help='optional svo file')
    parser.add_argument('--img_size', type=int, default=416, help='inference size (pixels)')
    parser.add_argument('--conf_thres', type=float, default=0.4, help='object confidence threshold')
    opt = parser.parse_args()

    with torch.no_grad():
        coordinated_target_dict = detector.object_detection(label, 25, opt)
        angle = find_angle(coordinated_target_dict[label])
        print("angle :", angle)

if __name__ == '__main__':
    main()
