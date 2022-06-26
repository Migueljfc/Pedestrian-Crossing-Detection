#!/usr/bin/env python3


import jetson.inference
import jetson.utils

import argparse
import sys
import time

import socket

import os


# parse the command line
parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.",
                                 formatter_class=argparse.RawTextHelpFormatter, epilog=jetson.inference.detectNet.Usage() +
                                 jetson.utils.videoSource.Usage() + jetson.utils.videoOutput.Usage() + jetson.utils.logUsage())

parser.add_argument("input_URI", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output_URI", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="ssd-mobilenet-v2", help="pre-trained model to load (see below for options)")
parser.add_argument("--overlay", type=str, default="box,labels,conf", help="detection overlay flags (e.g. --overlay=box,labels,conf)\nvalid combinations are:  'box', 'labels', 'conf', 'none'")
parser.add_argument("--threshold", type=float, default=0.5, help="minimum detection threshold to use")

is_headless = ["--headless"] if sys.argv[0].find('console.py') != -1 else [""]

try:
        opt = parser.parse_known_args()[0]
except:
        print("")
        parser.print_help()
        sys.exit(0)

s=socket.socket()
host='10.0.0.1'
port=7000



# create video output object 
output = jetson.utils.videoOutput(opt.output_URI, argv=sys.argv+is_headless)

# load the object detection network
net = jetson.inference.detectNet(opt.network, sys.argv, opt.threshold)

# create video sources
input = jetson.utils.videoSource(opt.input_URI, argv=sys.argv)
try:
            s.connect((host,port))
except:
        print("###############Server is not running###############")

#time.sleep(15)
# process frames until the user exits
while True:
        persons = 0
        # capture the next image
        img = input.Capture()

        # detect objects in the image (with overlay)
        detections = net.Detect(img, overlay=opt.overlay)

        # print the detections
        #print("detected {:d} objects in image".format(len(detections)))

        for detection in detections:
                #print(detection)
                #if detection.ClassID == 1:
                        #print("PERSON")
                        #persons = persons + 1
                persons = persons + 1
        print("********Persons detected = " + str(persons))

        data = str(persons)
        try:
                s.send(data.encode())
                print("SEND")
        except:
                print("SEND DATA ERROR")

        # render the image
        output.Render(img)

        # update the title bar
        output.SetStatus("{:s} | Network {:.0f} FPS".format(opt.network, 30))
        #net.GetNetworkFPS()
        # print out performance info
        #net.PrintProfilerTimes()

        # exit on input/output EOS
        if not input.IsStreaming() or not output.IsStreaming():
                break

s.shutdown(socket.SHUT_RDWR)
s.close()
                                                                                                                             