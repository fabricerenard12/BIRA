import record, algorithm
import detector
import argparse
import torch
import faulthandler
faulthandler.enable()

def main():
    text = record.transcribe_directly()
    print(text)

if __name__ == '__main__':
    main()
    