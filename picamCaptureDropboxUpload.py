#!/usr/bin/env python3.4

import sys, os
import time
import picamera

# Initialise camera
cam = picamera.PiCamera()

# Enable send commands to be run on command line
def run(cmd):
    print("Run: " + cmd)
    subprocess.call([cmd], shell = True)

# Create a camera object and capture image using generated filename
def camCapture(filename):
    with picamera.PiCamera as camera:
        # camera.resolution = size
        camera.resolution = (640, 480)
        print("Image: %s.jpg"%filename)
        time.sleep(2)
        camera.capture(filename, format='jpeg')
        print("Image Captured and saved ...")

# Generate timestamp string generating name for photos
def timestamp():
    tstring = datetime.datetime.now()
    print("Filename generated ...")
    return tstring.strftime("%Y%m%d_%H%M%S")


# Delete file
def deleteLocal(filename):
    os.system("rm " + filename)
    print("File: " + filename + " deleted ...")

def main():

    # Generate name for file based on current time
    filename = timestamp()

    # Capture photo
    camCapture(filename)

    # Upload photo to Dropbox
    #upload(filename)

    # Delete local copy of photo
    #deleteLocal(filename)

    print("Done")


if __name__ == '__main__':
    main()






