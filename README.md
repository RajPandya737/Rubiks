# Rubik's Cube Solver

## Description

This program aims to take photos of each side of your rubik's cube and give you the solution while also simulating it in 3-D space. Using openCV, numpy, matplotlib, colormath, and many other technologies, never before has solving a rubik's cube been as easy as it is right now. Take a look at the youtube video explaining the creation of this project and a short tutorial on how to use it.

## Link to the YouTube video about this project is [here](https://www.youtube.com/watch?v=8CAep-V3u5w)


## Installation

To use the Rubik's Cube Solver, follow these steps to set up the project:

1. Clone this repository to your local machine:
```bash
git clone https://github.com/RajPandya737/Rubiks-Cube-Solver.git
```
2. Change to the project directory:
```bash
cd Rubiks-Cube-Solver
```

3. The project utilizes many libraries such as openCV, numpy, pillow, colormath, matplotlib, and many more. Ensure you have all of them downloaded by running

```bash
pip install -r requirements.txt
```

4. Change to the main directory:
```bash
cd RubiksCubeSolver
```

5. Run the program, please read the usage part of this file before continuing:
```bash
python main.py
```


## Usage

To use the Rubik's Cube Solver, follow the installation steps:

1. Start with a scrambled rubik's cube you do not know how to solve

2. Run the file, whithin the terminal, you will be asked to calibrate your cube, if this is your first time running the program, it is highly recommended.

3. If you choose yes, scan the center of each face of the desired color the camera window asks, it will appear as the title of the window:

4. You will then be shown a tutorial of how to use the program, here is a quick recap, when shwoing the sides with a center color yellow or white, red should face upwards, in all other cases, white should be facing upwards.

5. Scan your cube in any order you like, just follow the rules from step 3

6. A window will appear with your cube and its solution, follow the steps and your cube will be solved.

7. For those unfamiliar with rubiks cube notation, this video explains it well: [Rubiks Cube Notation Explained](https://www.youtube.com/watch?v=24eHm4ri8WM)

8. If you would like to exit the program at any time, press the 'q' key while the camera is open, or close out of the program with your mouse while the simulation is open.


## Project Structure
The project consists of the following files inside of the RubiksCube folder:

1. `main.py`: The main Python script.
2. `cube.py`: The file containing the Rubiks cube class and the Cubie class.
3. `config.py`: A file containing all constants used in the program.
4. `color_diff.py`: A file containing color math operations.
5. `matplot_img.py`: A file containing the Img_MPL class.
6. `cube_renderer.py`: A file containing the class that renders the cube in MPL
7. `colors.json`: JSON file to store user color data
8. `README.md`: This file, providing an overview of the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


