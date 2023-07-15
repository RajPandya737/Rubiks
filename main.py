import cv2
from config import *

def main():
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
            # Outline, will probably use for loops later, if your reading this, it means im too lazy and havent done it yet.

            cv2.rectangle(frame, (50, 50), (300, 300), BOX_COLOR, 2)  

            # Top Row
            cv2.rectangle(frame, (50, 50), (133, 133), BOX_COLOR, 2)  
            cv2.rectangle(frame, (133, 50), (216, 133), BOX_COLOR, 2)  
            cv2.rectangle(frame, (216, 50), (300, 133), BOX_COLOR, 2)  

            # Middle Row

            cv2.rectangle(frame, (50, 133), (133, 216), BOX_COLOR, 2)  
            cv2.rectangle(frame, (133, 133), (216, 216), BOX_COLOR, 2)  
            cv2.rectangle(frame, (216, 133), (300, 216), BOX_COLOR, 2)  

            # Bottom Row

            cv2.rectangle(frame, (50, 216), (133, 300), BOX_COLOR, 2)  
            cv2.rectangle(frame, (133, 216), (216, 300), BOX_COLOR, 2)  
            cv2.rectangle(frame, (216, 216), (300, 300), BOX_COLOR, 2)  

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

main()