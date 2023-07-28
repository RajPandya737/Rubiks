import json

# Color of the webcam box // Black
BOX_COLOR = (0, 0, 0)

# Edges of the box on the camera
LEFT = 50
TOP = 50
RIGHT = 300
BOTTOM = 300

# Spacing between the lines in the box, since its a square should be symetric up & down
SPACING = (RIGHT - LEFT) // 3

# Width of ther border of the square
BORDER_THICKNESS = 2

# Colors
with open("colors.json", "r") as file:
    color_data = json.load(file)

WHITE = color_data["WHITE"]
RED = color_data["RED"]
BLUE = color_data["BLUE"]
ORANGE = color_data["ORANGE"]
GREEN = color_data["GREEN"]
YELLOW = color_data["YELLOW"]
