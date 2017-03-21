#!/usr/bin/env python3.4

import os
import time
import datetime
import picamera

# Create a camera object and capture image using generated filename
def camCapture(filename):
    with picamera.PiCamera as camera:
        camera.resolution = (640, 480)
        print("Photo: %s.jpg"%filename)
        time.sleep(2)
        camera.capture(filename + '.jpg', format='jpeg')
        print("Photo captured and saved ...")

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
