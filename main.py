import cv2
from config import *
import numpy as np
from PIL import Image
import os
import math
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color
from color_diff import *


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
                    cv2.rectangle(frame, (LEFT + col * SPACING, TOP + row*SPACING), (LEFT + (col+1) * SPACING, TOP + (row+1) * SPACING), BOX_COLOR, BORDER_THICKNESS)

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
        delete_img (f"sides/side{n}.jpg")

def delete_img (path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("Not Found")


def squarify(n):
    image = Image.open(f"cropped_sides/cside{n}.jpg")

    # Turn each images sides into 9 squares with their own color
    for i in range(3):
        for j in range(3):    
            # Coordinates for cropping 
            left = j * SPACING + SPACING // 4
            top = i * SPACING + SPACING // 4
            right = left + SPACING // 2
            bottom = top + SPACING // 2
                
            cropped_image = image.crop((left, top, right, bottom))
                
            # Save the cropped image
            chunk_number = i * 3 + j + 1
            cropped_image.save(f"squares/cside{chunk_number}.jpg")

    
    
def avg_color (path):
    # Turns the image into a 1x1 pixel which automatically takes the average pixel value
    image = Image.open(path)
    resized_image = image.resize((1, 1))
    rgb = resized_image.getpixel((0, 0))
    return rgb

def real_color (avg):
    colors_hash = {
        'White': (255, 255, 255),
        'Red': (190, 60, 20),
        'Blue': (121, 177, 201),
        'Orange': (255, 85, 37),
        'Green': (25, 155, 76),
        'Yellow': (254, 213, 47)
    }
# Basically a bunch of annopying conversions, convert rgb to sRGB then to 
# Lab Colors so you can finally compare them using a Delta E equation
# Find which color is the closest (lower delta E means closer color) and 
# return a bunch of potentially useful information about that

    avg = sRGBColor(avg[0], avg[1], avg[2]) 
    lab_color = convert_color(avg, LabColor)
    red_avg = lab_color.lab_l
    green_avg = lab_color.lab_a
    blue_avg = lab_color.lab_b
    c1 = LabColor(red_avg, green_avg, blue_avg)

    close_col = None
    close = float('inf')
    for color_name, color in colors_hash.items(): 
        stock_color = sRGBColor(color[0], color[1], color[2])
        stock_color = convert_color(stock_color, LabColor)
        red_stock, green_stock, blue_stock = stock_color.lab_l, stock_color.lab_a, stock_color.lab_b
        c2 = LabColor(red_stock, green_stock, blue_stock)

        result = delta_e_cie1976(c1, c2)
        if result < close:
            close = result
            close_col = (color, color_name)
    return close_col[0], close_col[1], close, avg


def main():
    get_cube() # method to get the cubes photos and screenshots
    convert_to_img()
    squarify(1)
    print(real_color(avg_color(f"squares/cside{1}.jpg")))


if __name__ == "__main__":
    main()