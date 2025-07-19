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

faulthandler.enable()

def find_angle(coordinated_target_list:np.ndarray) -> int:

   # x = trim_mean(coordinated_target_list[:,0], proportiontocut=0.1)
   # z = trim_mean(coordinated_target_list[:,2], proportiontocut=0.1)

    x = retrieve_data.get_distance2(coordinated_target_list[:,0])
    z = retrieve_data.get_distance2(coordinated_target_list[:,2])
    

    angle_rad = math.atan(x / z)

    # Convert radians to degrees
    angle_deg = math.degrees(angle_rad)
    print(angle_deg)
    return angle_deg

def find_angle2() -> int:
    x = retrieve_data.get_distance(0) 
    y = retrieve_data.get_distance(1)
    z = retrieve_data.get_distance(2)
    angle_rad = math.atan(x/z)

    # Convert radians to degrees
    angle_deg = math.degrees(angle_rad)
    print(angle_deg)
    return angle_deg


def main():
    #text = speech_to_text.transcribe_directly()
    text = "personne"
    print(text)
    label = algorithm.string_to_label(text)
    #label = 0

    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', type=str, default='../models/yolov8n.pt', help='model.pt path(s)') #A modifier pour changer de modele
    parser.add_argument('--svo', type=str, default=None, help='optional svo file')
    parser.add_argument('--img_size', type=int, default=416, help='inference size (pixels)')
    parser.add_argument('--conf_thres', type=float, default=0.4, help='object confidence threshold')
    opt = parser.parse_args()

    with torch.no_grad():
        coordinated_target_list = detector.object_detection(0, 25, opt)
        angle = find_angle(coordinated_target_list)
        angle2 = find_angle2()
        print("angle :", angle)
        print("angle2 :", angle2)
    


if __name__ == '__main__':
    main()
    
    # UART.send_data_through_UART(-angle)
    #UART.send_data_through_UART(input())
    # input("Press Enter to end the code...")
    # UART.send_data_through_UART(angle)


