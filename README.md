# Geometric Shape Calculator

## PROJECT OVERVIEW

A simple Python-based Geometric Shape Calculator that calculates areas, volumes, perimeters, surface areas, and other measurements for different geometric shapes.

The program provides a menu of 12 geometric shapes, accepts user input, performs the required calculation, displays the result, and maintains a calculation history during the program run. 

---

 ## Features

- 12 Geometric Shapes — Supports Circle, Rectangle, Square, Triangle, Trapezium, Parallelogram, Cube, Cuboid, Cylinder, Cone, Sphere, and Hemisphere.
- Area Calculation — Calculates the area of various 2D geometric shapes.
- Volume Calculation — Calculates the volume of 3D geometric shapes.
- Perimeter Calculation — Calculates the perimeter of applicable 2D shapes.
- Surface Area Calculation — Calculates surface or curved surface area for supported 3D shapes.
- Formula Display — Displays the formula used for the selected shape.
- Random Shape Suggestion — Randomly suggests a geometric shape for calculation.
- Calculation History — Stores and displays completed calculations during the program session.
- Date & Time Display — Shows the current date and time.
- Random Number Generator — Generates a random number between 1 and 100.
- Input Validation — Checks that dimensions such as radius, height, length, breadth, and side are positive.
- Invalid Choice Handling — Provides an error message when an invalid menu option is selected.
- Python Math Functions — Uses Python's `math` module for accurate mathematical calculations.
- Python Data Structures — Demonstrates the use of tuples, lists, sets, and dictionaries.
- Simple CLI Interface — Easy-to-use command-line interface with clear menus and instructions.

---

## Supported Shapes
No.	Shape	Calculation
1	Circle	Area, Circumference
2	Rectangle	Area, Perimeter
3	Square	Area, Perimeter
4	Triangle	Area
5	Trapezium	Area
6	Parallelogram	Area
7	Cube	Volume, Surface Area
8	Cuboid	Volume, Surface Area
9	Cylinder	Volume, Curved Surface Area
10	Cone	Volume, Slant Height
11	Sphere	Volume, Surface Area
12	Hemisphere	Volume, Curved Surface Area

## Formulas Used
1. Circle

Area

π × r²


Circumference

2 × π × r

2. Rectangle

Area

length × breadth


Perimeter

2 × (length + breadth)

3. Square

Area

side²


Perimeter

4 × side

4. Triangle

Area

½ × base × height

5. Trapezium

Area

½ × (a + b) × height

6. Parallelogram

Area

base × height

7. Cube

Volume

side³


Surface Area

6 × side²

8. Cuboid

Volume

length × breadth × height


Surface Area

2 × (lb + bh + hl)

9. Cylinder

Volume

π × r² × h


Curved Surface Area

2 × π × r × h

10. Cone

Volume

(π × r² × h) / 3


Slant Height

√(r² + h²)

11. Sphere

Volume

(4 × π × r³) / 3


Surface Area

4 × π × r²

12. Hemisphere

Volume

(2 × π × r³) / 3


Curved Surface Area

2 × π × r²

## Technologies Used

Python 3

math module

random module

datetime module

All modules used in the program are part of Python's standard library, so no external packages are required.

📁 Project Structure
Geometric-Shape-Calculator/\
│ \
├── geometric_shape_calculator.py\
└── README.md


Replace geometric_shape_calculator.py with the actual filename if your Python file has a different name.
## Technologies/Tools Used

* Python 3
* Python functions
* Conditional statements
* Loops
* Lists
* Dictionaries
* Input validation
* Console/Terminal
* Git and GitHub for version control

The current project does not require any external Python libraries.

---

## Installation and Setup

Follow the steps below to install and run the project on your computer.

### Step 1: Install Python

Download and install Python 3 on your computer.

After installation, open Command Prompt / Terminal and check whether Python is installed:

```bash
python --version
```

If required, use:

```bash
python3 --version
```

You should see the installed Python version.

---
### Step 2: Download the Project

You can either clone the GitHub repository or download it as a ZIP file.

#### Option 1 — Clone the Repository

```bash
git clone <https://github.com/Pranavvidyarthi-09/GEOMETRICAL-SHAPE-CALCULATOR.git>
```

Navigate to the project folder:

```bash
cd vityarthiproject
```

#### Option 2 — Download ZIP

1. Open the GitHub repository.
2. Click **Code**.
3. Select **Download ZIP**.
4. Extract the downloaded ZIP file.
5. Open the extracted project folder.

---

### Step 3: Verify the Project Files

Make sure the project contains:

```text
project1.py
README.md
statement.md
```

---


## Instruction for Testing
The Geometric Shape Calculator can be tested directly through the Console/Terminal. The following tests can be used to check calculations, input validation, and program behavior.

1. Run the Program
Open a terminal in the project folder and run:

python geometric_shape_calculator.py

If your Python command is python3, use:

python3 geometric_shape_calculator.py

The calculator should display the main menu with 12 geometric shapes.

2. Test Shape Selection
Enter different menu choices from 1 to 12.

Example:

Enter your choice (1-12): 1

The program should open the calculation section for the selected shape.

Test all options:

Choice	Shape
1	Circle
2	Rectangle
3	Square
4	Triangle
5	Trapezium
6	Parallelogram
7	Cube
8	Cuboid
9	Cylinder
10	Cone
11	Sphere
12	Hemisphere

3. Test Circle Calculation
Choose:

Enter your choice (1-12): 1
Enter radius: 5

Expected result:

Shape: Circle
Area: 78.53981633974483
Circumference: 31.41592653589793

4. Test Rectangle Calculation
Choose:

Enter your choice (1-12): 2
Enter length: 10
Enter breadth: 5

Expected result:

Shape: Rectangle
Area: 50.0
Perimeter: 30.0

5. Test Square Calculation
Choose:

Enter your choice (1-12): 3
Enter side: 5

Expected result:

Shape: Square
Area: 25.0
Perimeter: 20.0

6. Test 3D Shape Calculations
Test the following shapes with positive values:

Cube

Cuboid

Cylinder

Cone

Sphere

Hemisphere

Check that the program displays the appropriate volume and surface-area-related result.

7. Test Invalid Menu Input
Enter a number outside the valid range:

Enter your choice (1-12): 15

Expected behavior:

Please choose a number between 1 and 12.

The program should ask for the choice again instead of crashing.

8. Test Text Input
Enter text instead of a menu number:

Enter your choice (1-12): hello

Expected behavior:

Please enter a whole number, for example: 1, 2 or 12.

The program should continue running and ask for the choice again.

9. Test Zero and Negative Values
For example:

Enter radius: 0

or:

Enter radius: -5

Expected behavior:

Please enter a number greater than 0.

The program should not accept zero or negative dimensions.

10. Test Invalid Measurement Input
Enter text instead of a measurement:

Enter radius: abc

Expected behavior:

That's not a valid number. Please try again.

The program should ask for the radius again.

11. Test Decimal Values
Test the calculator using decimal values:

Enter radius: 5.5

The program should accept the value and calculate the result correctly.

12. Test Random Shape Suggestion
Every time the program starts, check:

Random Shape Suggestion
-----------------------
You can try: Circle

The suggested shape should be one of the 12 available shapes.

13. Test Date and Time
When the program starts, verify that the terminal displays:

Date: YYYY-MM-DD
Time: HH:MM:SS

The displayed date and time should match the computer's current date and time.

14. Test Formula Display
After completing a calculation, check that the program displays the selected shape and its formula.

CALCULATION DETAILS
=============================================
Selected Shape: Circle
Formula: Area = π × r × r

15. Test Calculation History
After completing a calculation, check the Calculation History section.

Example:

Calculation History
---------------------------------------------
Shape: Circle
Result: 78.53981633974483

The completed calculation should appear in the history.

16. Final Testing Checklist
Before submitting the project, verify:

 Program starts successfully in the terminal.

 All 12 shapes are displayed.

 Menu choices 1–12 work correctly.

 Area calculations work correctly.

 Perimeter calculations work correctly.

 Volume calculations work correctly.

 Surface-area calculations work correctly.

 Positive decimal values are accepted.

 Zero values are rejected.

 Negative values are rejected.

 Invalid text input does not crash the program.

 Invalid menu choices are handled.

 Random shape suggestion works.

 Date and time are displayed.

 Formula is displayed.

 Calculation history is displayed.

 Program ends with the thank-you message.

CALCULATION DETAILS
=============================================
Selected Shape: Circle
Formula: Area = π × r × r

15. Test Calculation History
After completing a calculation, check the Calculation History section.

Example:

Calculation History
---------------------------------------------
Shape: Circle
Result: 78.53981633974483

The completed calculation should appear in the history.

16. Final Testing Checklist
Before submitting the project, verify:

 Program starts successfully in the terminal.

 All 12 shapes are displayed.

 Menu choices 1–12 work correctly.

 Area calculations work correctly.

 Perimeter calculations work correctly.

 Volume calculations work correctly.

 Surface-area calculations work correctly.

 Positive decimal values are accepted.

 Zero values are rejected.

 Negative values are rejected.

 Invalid text input does not crash the program.

 Invalid menu choices are handled.

 Random shape suggestion works.

 Date and time are displayed.

 Formula is displayed.

 Calculation history is displayed.

 Program ends with the thank-you message.

========================================
       GEOMETRIC SHAPE CALCULATOR
========================================
1. Circle
2. Rectangle
3. Square
4. Triangle
5. Trapezium
6. Parallelogram
7. Cube
8. Cuboid
9. Cylinder
10. Cone
11. Sphere
12. Hemisphere
========================================


The program also generates a random shape suggestion:

Random Shape Number: 3
Random Shape Suggestion: Square


The user can then select a shape:

Enter your choice: 1


For a circle, the program asks for the radius:

Enter radius: 5


The output may look like:

Shape = Circle
Area = 78.53981633974483
Circumference = 31.41592653589793


The selected shape and its formula are displayed afterward:

========================================
Selected Shape: Circle
Formula: Area = 3.14 * r * r
========================================

## Calculation History

The program stores completed calculations in the history list.

For example:

Calculation History:
[('Circle', 78.53981633974483)]


If the calculation is not completed because of invalid input, the program displays:

No calculation was completed


Note: The history is stored only while the program is running. It is not saved to a file or database.

## Random Features

The program uses Python's random module for two purposes.

Random Shape Suggestion

A number from 1 to 12 is generated:

random_number = random.randint(1, 12)


This number is used to suggest one of the available shapes.

Random Number

At the end of the program, another random number from 1 to 100 is generated:

random_number = random.randint(1, 100)

## Date and Time

The program displays the current date and time using Python's datetime module.

Example:

Date: 2026-09-27
Time: 01:02:30

## Input Validation

The program checks that dimensions such as radius, length, breadth, base, height, and side are greater than zero.

For example:

Enter radius: -5
Radius must be greater than 0


This prevents calculations from being performed with invalid negative dimensions.

# Current Limitations

The program accepts only one calculation per execution.

Calculation history is not permanently saved.

Entering non-numeric input such as abc can cause a ValueError.

The formula dictionary uses 3.14 for display, while calculations use math.pi.

The sphere volume formula displayed in the formulas dictionary should mathematically be interpreted as (4 × π × r³) / 3.

The program does not currently provide an option to repeat calculations without restarting.

The shape_set is used to count the total number of shapes but does not otherwise affect calculations.

* Possible Future Improvements

The project could be improved by adding:

* A loop to perform multiple calculations in one execution

* Saving calculation history to a text, CSV, or JSON file

* A dedicated history menu

* Better handling of non-numeric input using try-except

* A graphical user interface using Tkinter

* More geometric shapes

* Additional measurements such as total surface area

* Rounded results for easier reading

* Cleaner and more reusable functions for each shape

* More detailed formula descriptions

* An option to exit the calculator from the menu

* Learning Objectives

# This project demonstrates several important Python concepts:

Variables and data types

User input with input()

Conditional statements

if, elif, and else

Tuples

Sets

Dictionaries

Lists

List methods such as append()

Mathematical calculations

Built-in Python modules

Random number generation

Date and time handling

Basic input validation

Functions from the math module

 ## Project Purpose

The main purpose of this project is to create a beginner-friendly Python application for performing common geometric calculations while practicing fundamental programming concepts.

It can also be used as a school/college Python project or as a beginner programming exercise.

---

## Screenshorts

### User Menu
<

 




Thank you for using the Geometric Shape Calculator!
