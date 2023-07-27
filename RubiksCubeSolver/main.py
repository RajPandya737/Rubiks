import cv2
from config import *
import numpy as np
from PIL import Image
import os
import math
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color
from color_diff import *
import shutil
from cube import *
import matplotlib.pyplot as plt
from matplot_img import Img_MPL
from mpl_toolkits.mplot3d import Axes3D
import sys
from cube_renderer import Cube_MPL
import json
import easygui as eg

def show_directions():
    img = Img_MPL("images/instructions.png", "Tutorial")
    img.show_img()

# When showing the cube to the camera, prioritize the white center on top, but if you are showing white or yellow, red should be on top
def get_cube():

    webcam = cv2.VideoCapture(0)  # Default camera on your system
    side = 1  # Pics taken so far // increments by 1 every time photo taken

    # Check if opened correctly
    if not webcam.isOpened():
        print("Failed to open the camera")
        exit()

    #cv2.namedWindow("Camera Feed")  # Create a window to display the camera feed

    while True:
        ret, frame = webcam.read()  # Gets the frame

        if ret:

            # Clever little code snippet basically makes the whole square box
            for row in range(3):
                for col in range(3):
                    cv2.rectangle(
                        frame,
                        (LEFT + col * SPACING, TOP + row * SPACING),
                        (LEFT + (col + 1) * SPACING, TOP + (row + 1) * SPACING),
                        BOX_COLOR,
                        BORDER_THICKNESS,
                    )

            cv2.imshow("Camera Feed Full Cube", frame)  # Display

            # If space bar is pressed, takes a photo, this method can be found in 'capture.py'
            if cv2.waitKey(1) & 0xFF == ord(" "):
                cv2.imwrite(f"sides/side{side}.jpg", frame)
                print("Photo captured!")
                side += 1

            if side == 7:  # End when the all sides photos have been taken
                webcam.release()
                cv2.destroyAllWindows()
                break

        # Wait for the 'q' key to be pressed to exit the loop
        if cv2.waitKey(1) & 0xFF == ord("q") or side == 7:
            break

    # Release the video capture
    webcam.release()
    cv2.destroyAllWindows()


def convert_to_img():
    try:
        # We do a bit of cropping around here
        for n in range(1, 7):
            image = Image.open(f"sides/side{n}.jpg")
            cropped_image = image.crop((LEFT, TOP, RIGHT, BOTTOM))
            cropped_image.save(f"cropped_sides/cside{n}.jpg")
            delete_img(f"sides/side{n}.jpg")
    except FileNotFoundError:
        print("The file was not found")
        sys.exit()


def delete_img(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        print("Not Found")


def clean_directory():
    # gets rid of all the images in the directory
    folder_path = os.getcwd()
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".jpg"):
                file_path = os.path.join(root, filename)
                os.remove(file_path)


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


# just an easy function to use, made it lambda cause its shorter
color_function = lambda x: real_color(avg_color(x))[4]


def avg_color(path):
    # Turns the image into a 1x1 pixel which automatically takes the average pixel value
    image = Image.open(path)
    resized_image = image.resize((1, 1))
    rgb = resized_image.getpixel((0, 0))
    return rgb


def real_color(avg):
    # Basically a bunch of annopying conversions, convert rgb to sRGB then to
    # Lab Colors so you can finally compare them using a Delta E equation
    # Find which color is the closest (lower delta E means closer color) and
    # return a bunch of potentially useful information about that
    # In order of what is returned, it is the rgb of the rubiks cube color,
    # the name of the color in full, how close it was, the average color of the image analyzed,
    # and the shortform of the color (example Blue become b)
    colors_hash = {
        "White": WHITE,
        "Red": RED,
        "Blue": BLUE, 
        "Orange": ORANGE, 
        "Green": GREEN, 
        "Yellow": YELLOW 
    }

    color_to_abreviation = {
        "White": "w",
        "Red": "r",
        "Blue": "b",
        "Orange": "o",
        "Green": "g",
        "Yellow": "y",
    }


    avg = sRGBColor(avg[0], avg[1], avg[2])
    lab_color = convert_color(avg, LabColor)
    red_avg = lab_color.lab_l
    green_avg = lab_color.lab_a
    blue_avg = lab_color.lab_b
    c1 = LabColor(red_avg, green_avg, blue_avg)

    close_col = None
    close = float("inf")
    for color_name, color in colors_hash.items():
        stock_color = sRGBColor(color[0], color[1], color[2])
        stock_color = convert_color(stock_color, LabColor)
        red_stock, green_stock, blue_stock = (
            stock_color.lab_l,
            stock_color.lab_a,
            stock_color.lab_b,
        )
        c2 = LabColor(red_stock, green_stock, blue_stock)

        result = delta_e_cie1976(c1, c2)
        if result < close:
            close = result
            close_col = (color, color_name)

    return close_col[0], close_col[1], close, avg, color_to_abreviation[close_col[1]]


def file_as_color():
    for side in range(1, 7):
        squarify(side)
        side_color = real_color(avg_color(f"squares/cside{5}.jpg"))[1]
        for n in range(1, 10):
            shutil.copyfile(f"squares/cside{n}.jpg", f"faces/{side_color}/cside{n}.jpg")
            delete_img(f"squares/cside{n}.jpg")


def convert_to_np():

    # We can start to build the cube from the yellow and white sides, these will always be opposite from each
    # other so if we create every other piece relative to these 2, everything should fit nicely (hopefully)

    #All the centers are already in the cubies list
    cubies = [
        Cubie(0, 0, 1, (None, None, "w"), "center"),
        Cubie(0, 0, -1, (None, None, "y"), "center"),
        Cubie(0, 1, 0, (None, "r", None), "center"),
        Cubie(0, -1, 0, (None, "o", None), "center"),
        Cubie(1, 0, 0, ("g", None, None), "center"),
        Cubie(-1, 0, 0, ("b", None, None), "center"),
    ]

    #White Side Cubies

    color_x = color_function(f"faces/Blue/cside{1}.jpg")
    color_y = color_function(f"faces/Red/cside{3}.jpg")
    color_z = color_function(f"faces/White/cside{1}.jpg")
    cubies.append(Cubie(-1, 1, 1, (color_x, color_y, color_z), "corner"))

    color_y = color_function(f"faces/Red/cside{2}.jpg")
    color_z = color_function(f"faces/White/cside{2}.jpg")
    cubies.append(Cubie(0, 1, 1, (None, color_y, color_z), "edge"))

    color_x = color_function(f"faces/Green/cside{3}.jpg")
    color_y = color_function(f"faces/Red/cside{1}.jpg")
    color_z = color_function(f"faces/White/cside{3}.jpg")
    cubies.append(Cubie(1, 1, 1, (color_x, color_y, color_z), "corner"))

    color_x = color_function(f"faces/Blue/cside{2}.jpg")
    color_z = color_function(f"faces/White/cside{4}.jpg")
    cubies.append(Cubie(-1, 0, 1, (color_x, None, color_z), "edge"))


    color_x = color_function(f"faces/Green/cside{2}.jpg")
    color_z = color_function(f"faces/White/cside{6}.jpg")
    cubies.append(Cubie(1, 0, 1, (color_x, None, color_z), "edge"))

    color_x = color_function(f"faces/Blue/cside{3}.jpg")
    color_y = color_function(f"faces/Orange/cside{1}.jpg")
    color_z = color_function(f"faces/White/cside{7}.jpg")
    cubies.append(Cubie(-1, -1, 1, (color_x, color_y, color_z), "corner"))

    color_y = color_function(f"faces/Orange/cside{2}.jpg")
    color_z = color_function(f"faces/White/cside{8}.jpg")
    cubies.append(Cubie(0, -1, 1, (None, color_y, color_z), "edge"))

    color_x = color_function(f"faces/Green/cside{1}.jpg")
    color_y = color_function(f"faces/Orange/cside{3}.jpg")
    color_z = color_function(f"faces/White/cside{9}.jpg")
    cubies.append(Cubie(1, -1, 1, (color_x, color_y, color_z), "corner"))

    
    # Center Cubies
    color_x = color_function(f"faces/Green/cside{6}.jpg")
    color_y = color_function(f"faces/Red/cside{4}.jpg")
    cubies.append(Cubie(1, 1, 0, (color_x, color_y, None), "edge"))
    
    color_x = color_function(f"faces/Blue/cside{4}.jpg")
    color_y = color_function(f"faces/Red/cside{6}.jpg")
    cubies.append(Cubie(-1, 1, 0, (color_x, color_y, None), "edge"))

    color_x = color_function(f"faces/Blue/cside{6}.jpg")
    color_y = color_function(f"faces/Orange/cside{4}.jpg")
    cubies.append(Cubie(-1, -1, 0, (color_x, color_y, None), "edge"))

    color_x = color_function(f"faces/Green/cside{4}.jpg")
    color_y = color_function(f"faces/Orange/cside{6}.jpg")
    cubies.append(Cubie(1, -1, 0, (color_x, color_y, None), "edge"))


    # Yellow Side Cubies

    color_x = color_function(f"faces/Blue/cside{7}.jpg")
    color_y = color_function(f"faces/Red/cside{9}.jpg")
    color_z = color_function(f"faces/Yellow/cside{3}.jpg")
    cubies.append(Cubie(-1, 1, -1, (color_x, color_y, color_z), "corner"))

    color_y = color_function(f"faces/Red/cside{8}.jpg")
    color_z = color_function(f"faces/Yellow/cside{2}.jpg")
    cubies.append(Cubie(0, 1, -1, (None, color_y, color_z), "edge"))

    color_x = color_function(f"faces/Green/cside{9}.jpg")
    color_y = color_function(f"faces/Red/cside{7}.jpg")
    color_z = color_function(f"faces/Yellow/cside{1}.jpg")
    cubies.append(Cubie(1, 1, -1, (color_x, color_y, color_z), "corner"))

    color_x = color_function(f"faces/Blue/cside{8}.jpg")
    color_z = color_function(f"faces/Yellow/cside{6}.jpg")
    cubies.append(Cubie(-1, 0, -1, (color_x, None, color_z), "edge"))


    color_x = color_function(f"faces/Green/cside{8}.jpg")
    color_z = color_function(f"faces/Yellow/cside{4}.jpg")
    cubies.append(Cubie(1, 0, -1, (color_x, None, color_z), "edge"))

    color_x = color_function(f"faces/Blue/cside{9}.jpg")
    color_y = color_function(f"faces/Orange/cside{7}.jpg")
    color_z = color_function(f"faces/Yellow/cside{9}.jpg")
    cubies.append(Cubie(-1, -1, -1, (color_x, color_y, color_z), "corner"))

    color_y = color_function(f"faces/Orange/cside{8}.jpg")
    color_z = color_function(f"faces/Yellow/cside{8}.jpg")
    cubies.append(Cubie(0, -1, -1, (None, color_y, color_z), "edge"))

    color_x = color_function(f"faces/Green/cside{7}.jpg")
    color_y = color_function(f"faces/Orange/cside{9}.jpg")
    color_z = color_function(f"faces/Yellow/cside{7}.jpg")
    cubies.append(Cubie(1, -1, -1, (color_x, color_y, color_z), "corner"))
    
    return Cube(cubies)


def color_tester_function():
    for n in range(1, 10):
        print(avg_color(f"cside{n}.jpg"))



def calibrate_colors():

    webcam = cv2.VideoCapture(0)  # Default camera on your system
    side = 1  # Pics taken so far // increments by 1 every time photo taken

    side_hash = {1: "White", 2: "Red", 3: "Blue", 4: "Orange", 5: "Green", 6: "Yellow"}
    # Check if opened correctly
    if not webcam.isOpened():
        print("Failed to open the camera")
        exit()

    cv2.namedWindow("Camera Feed")  # Create a window to display the camera feed
    print(f"Press display the {side_hash[side]} side and press the space bar to capture it")
    is_open = True
    while True:
        ret, frame = webcam.read()  # Gets the frame

        if ret:

            cv2.rectangle(frame, (LEFT, TOP), (LEFT + SPACING, TOP + SPACING), BOX_COLOR, BORDER_THICKNESS,)
            cv2.imshow("Camera Feed", frame)  # Display

            # If space bar is pressed, takes a photo, this method can be found in 'capture.py'
            if cv2.waitKey(1) & 0xFF == ord(" "):
                cv2.imwrite(f"centers/side{side}.jpg", frame)
                print("Photo captured!")
                side += 1
                if side != 7:
                    print(f"Press display the {side_hash[side]} side and press the space bar to capture it")

            if side == 7:  # End when the all sides photos have been taken
                webcam.release()
                cv2.destroyAllWindows()
                break

        # Wait for the 'q' key to be pressed to exit the loop
        if cv2.waitKey(1) & 0xFF == ord("q") or side == 7:
            break

    # Release the video capture
    webcam.release()
    cv2.destroyAllWindows()

def crop_centers():
    for n in range(1, 7):
        image = Image.open(f"centers/side{n}.jpg")
        cropped_image = image.crop((LEFT + SPACING//4, TOP + SPACING//4, LEFT+ 3*SPACING//4, TOP+ 3*SPACING//4))
        cropped_image.save(f"cropped_centers/cside{n}.jpg")
        delete_img(f"centers/side{n}.jpg")

def calibrate():
    print("Show the camera the center of the desired color, then press the space bar to take a photo.")
    calibrate_colors()
    crop_centers()
    center_colors()


def center_colors():
    color_data = {"WHITE" : avg_color(f"cropped_centers/cside1.jpg"),
                  "RED" : avg_color(f"cropped_centers/cside2.jpg"),
                  "BLUE" : avg_color(f"cropped_centers/cside3.jpg"),
                "ORANGE" : avg_color(f"cropped_centers/cside4.jpg"),
                "GREEN" : avg_color(f"cropped_centers/cside5.jpg"),
                "YELLOW" : avg_color(f"cropped_centers/cside6.jpg")
    }

    with open("colors.json", "w") as file:
        json.dump(color_data, file, indent=2)



def load_colors():
    global YELLOW, BLUE, GREEN, WHITE, RED, ORANGE
    with open("colors.json", "r") as file:
        color_data = json.load(file)

    WHITE = color_data["WHITE"]
    RED = color_data["RED"]
    BLUE = color_data["BLUE"]
    ORANGE = color_data["ORANGE"]
    GREEN = color_data["GREEN"]
    YELLOW = color_data["YELLOW"]

def create_missing_folders():
    required_folders = ["centers", "cropped_centers", "cropped_sides", "faces", "sides", "squares", "faces/Blue", "faces/Green", "faces/Orange", "faces/Red", "faces/White", "faces/Yellow"]

    for folder in required_folders:
        if not os.path.exists(folder):
            os.makedirs(folder)

def ask_calibration():
    welcome_message = "Welcome to the Rubik's Cube Solver!"
    choices = ["Yes", "No"]
    response = eg.buttonbox(welcome_message + "\nWould you like to calibrate the colors?", choices=choices)
    return response

def main():
    create_missing_folders()
    answer = ask_calibration()
    if answer == "Yes":
        calibrate()
    load_colors()
    clean_directory()
    show_directions()
    print("Time to scan the cube!")
    get_cube()  # method to get the cubes photos and screenshots
    convert_to_img()
    file_as_color()
    try:
        Cube = convert_to_np()
        #print(Cube.__str__())
        #print(solution)
        cube_simulation = Cube_MPL(Cube)
        cube_simulation.render()
    except:
        print("Error: Camera quality was too low, the colors could not be picked up, or cube is not solvable")
    
    #clean_directory()
         

if __name__ == "__main__":
    main()
    #color_tester_function()
    clean_directory()

