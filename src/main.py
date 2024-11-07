#import record, algorithm
import outputs.retrieve_data as retrieve_data
import detector
import argparse
import torch
import math
#import faulthandler
#faulthandler.enable()
def find_angle():
    x = retrieve_data.get_distance(0)
    print(x)
    y = retrieve_data.get_distance(1)
    z = retrieve_data.get_distance(2)
    angle_rad = math.atan(x/z)
    print(z)
    print(angle_rad)

    # Convert radians to degrees
    angle_deg = math.degrees(angle_rad)
    print(angle_deg)

def main():
    #text = record.transcribe_directly() + " pomme "
    #print(text)
    #label = algorithm.stringtoLabel(text)
    label = 0

    parser = argparse.ArgumentParser()
    parser.add_argument('--weights', type=str, default='../models/yolov8n.pt', help='model.pt path(s)') #A modifier pour changer de modele
    parser.add_argument('--svo', type=str, default=None, help='optional svo file')
    parser.add_argument('--img_size', type=int, default=416, help='inference size (pixels)')
    parser.add_argument('--conf_thres', type=float, default=0.4, help='object confidence threshold')
    opt = parser.parse_args()

    with torch.no_grad():
        detector.object_detection(0, 5, opt)
    





if __name__ == '__main__':
    main()
    find_angle()
