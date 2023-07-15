import cv2
from config import *
import numpy as np
from PIL import Image

def get_cube ():
    #gloablish variables
    webcam = cv2.VideoCapture(0)  # Default camera on your system
    side = 1 # Pics taken so far // increments by 1 every time photo taken

    # Check if opened correctly
    if not webcam.isOpened():
        print("Failed to open the camera")
        exit()

    # Create a window to display the camera feed
    cv2.namedWindow("Camera Feed")



    while True:
        # Get frame
        ret, frame = webcam.read()

        if ret:

            #Clever little code snippet basically makes the whole square box 
            for row in range (3):
                for col in range(3):
                    cv2.rectangle(frame, (LEFT + col * SPACING, TOP + row*SPACING), (LEFT + (col+1) * SPACING, TOP + (row+1) * SPACING), BOX_COLOR, 2)
 

            # Display 
            cv2.imshow("Camera Feed", frame)

            # If space bar is pressed, takes a photo, this method can be found in 'capture.py'

            if cv2.waitKey(1) & 0xFF == ord(' '):
                cv2.imwrite(f"sides/side{side}.jpg", frame)
                print("Photo captured!")
                side+=1

            if side == 7:
                break

        # Wait for the 'q' key to be pressed to exit the loop

        if cv2.waitKey(1) & 0xFF == ord('q') or side == 7:
            break

    # Release the video capture
    webcam.release()
    cv2.destroyAllWindows()

def convert_to_img ():
    for n in range(1, 7):
        image = Image.open(f"sides/side{n}.jpg")

        cropped_image = image.crop((LEFT, TOP, RIGHT, BOTTOM))
        cropped_image.save(f"cropped_sides/cside{n}.jpg")


def main():
    get_cube() # method to get the cubes photos and screenshots
    convert_to_img()



if __name__ == "__main__":
    main()