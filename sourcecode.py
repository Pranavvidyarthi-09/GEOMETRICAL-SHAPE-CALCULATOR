import random
import datetime
import math

print("========================================")
print("       GEOMETRIC SHAPE CALCULATOR")
print("========================================")
print("1. Circle")
print("2. Rectangle")
print("3. Square")
print("4. Triangle")
print("5. Trapezium")
print("6. Parallelogram")
print("7. Cube")
print("8. Cuboid")
print("9. Cylinder")
print("10. Cone")
print("11. Sphere")
print("12. Hemisphere")
print("========================================")

shapes = (
    "Circle", "Rectangle", "Square", "Triangle",
    "Trapezium", "Parallelogram", "Cube", "Cuboid",
    "Cylinder", "Cone", "Sphere", "Hemisphere"
)

formulas = {
    "Circle": "Area = π * r * r",
    "Rectangle": "Area = l * b",
    "Square": "Area = s * s",
    "Triangle": "Area = 0.5 * b * h",
    "Trapezium": "Area = 0.5 * (a + b) * h",
    "Parallelogram": "Area = b * h",
    "Cube": "Volume = s * s * s",
    "Cuboid": "Volume = l * b * h",
    "Cylinder": "Volume = π * r * r * h",
    "Cone": "Volume = (π * r * r * h) / 3",
    "Sphere": "Volume = (4 * π * r * r * r) / 3",
    "Hemisphere": "Volume = (2 * π * r * r * r) / 3"
}

history = []

shape_set = {
    "Circle", "Rectangle", "Square", "Triangle",
    "Trapezium", "Parallelogram", "Cube", "Cuboid",
    "Cylinder", "Cone", "Sphere", "Hemisphere"
}


# -----------------------------------------------------------
# INPUT VALIDATION FUNCTIONS
# ---------------------------------------------------------------

def get_positive_number(message):
    """
    Get a positive number from the user.
    Keeps asking until valid input is entered.
    """
    while True:
        try:
            value = float(input(message))

            if value > 0:
                return value
            else:
                print("Invalid input! Value must be greater than 0.")

        except ValueError:
            print("Invalid input! Please enter a valid number.")


def get_choice():
    """
    Get a valid menu choice from 1 to 12.
    """
    while True:
        try:
            choice = int(input("Enter your choice (1-12): "))

            if 1 <= choice <= 12:
                return choice
            else:
                print("Invalid choice! Please enter a number from 1 to 12.")

        except ValueError:
            print("Invalid input! Please enter a whole number from 1 to 12.")


# =======================================================
# RANDOM SHAPE SUGGESTION
# ============================================================

random_shape_number = random.randint(1, 12)

print("Random Shape Number:", random_shape_number)
print("Random Shape Suggestion:", shapes[random_shape_number - 1])

# Get validated menu choice
choice = get_choice()


# ==============================================================
# Date time
# ============================================================--

current_time = datetime.datetime.now()

print("Date:", current_time.date())
print("Time:", current_time.strftime("%H:%M:%S"))


# ============================================================
# CIRCLE
# ============================================================

if choice == 1:

    r = get_positive_number("Enter radius: ")

    area = math.pi * r * r
    circumference = 2 * math.pi * r

    print("Shape = Circle")
    print("Area =", area)
    print("Circumference =", circumference)

    history.append(("Circle", area))


# ==========================================================
# RECTANGLE
# ============================================================

elif choice == 2:

    l = get_positive_number("Enter length: ")
    b = get_positive_number("Enter breadth: ")

    area = l * b
    perimeter = 2 * (l + b)

    print("Shape = Rectangle")
    print("Area =", area)
    print("Perimeter =", perimeter)

    history.append(("Rectangle", area))


# ============================================================
# SQUARE
# ============================================================

elif choice == 3:

    s = get_positive_number("Enter side: ")

    area = s * s
    perimeter = 4 * s

    print("Shape = Square")
    print("Area =", area)
    print("Perimeter =", perimeter)

    history.append(("Square", area))


# ============================================================
# TRIANGLE
# ============================================================

elif choice == 4:

    b = get_positive_number("Enter base: ")
    h = get_positive_number("Enter height: ")

    area = 0.5 * b * h

    print("Shape = Triangle")
    print("Area =", area)

    history.append(("Triangle", area))


# ============================================================
# TRAPEZIUM
# ============================================================

elif choice == 5:

    a = get_positive_number("Enter first parallel side: ")
    b = get_positive_number("Enter second parallel side: ")
    h = get_positive_number("Enter height: ")

    area = 0.5 * (a + b) * h

    print("Shape = Trapezium")
    print("Area =", area)

    history.append(("Trapezium", area))


# ============================================================
# PARALLELOGRAM
# ============================================================

elif choice == 6:

    b = get_positive_number("Enter base: ")
    h = get_positive_number("Enter height: ")

    area = b * h

    print("Shape = Parallelogram")
    print("Area =", area)

    history.append(("Parallelogram", area))


# ============================================================
# CUBE
# ============================================================

elif choice == 7:

    s = get_positive_number("Enter side: ")

    volume = s * s * s
    surface_area = 6 * s * s

    print("Shape = Cube")
    print("Volume =", volume)
    print("Surface Area =", surface_area)

    history.append(("Cube", volume))


# ============================================================
# CUBOID
# ============================================================

elif choice == 8:

    l = get_positive_number("Enter length: ")
    b = get_positive_number("Enter breadth: ")
    h = get_positive_number("Enter height: ")

    volume = l * b * h
    surface_area = 2 * (l * b + b * h + h * l)

    print("Shape = Cuboid")
    print("Volume =", volume)
    print("Surface Area =", surface_area)

    history.append(("Cuboid", volume))


# ============================================================
# CYLINDER
# ============================================================

elif choice == 9:

    r = get_positive_number("Enter radius: ")
    h = get_positive_number("Enter height: ")

    volume = math.pi * r * r * h
    curved_area = 2 * math.pi * r * h

    print("Shape = Cylinder")
    print("Volume =", volume)
    print("Curved Surface Area =", curved_area)

    history.append(("Cylinder", volume))


# ============================================================
# CONE
# ============================================================

elif choice == 10:

    r = get_positive_number("Enter radius: ")
    h = get_positive_number("Enter height: ")

    volume = (math.pi * r * r * h) / 3
    slant_height = math.sqrt(r * r + h * h)

    print("Shape = Cone")
    print("Volume =", volume)
    print("Slant Height =", slant_height)

    history.append(("Cone", volume))


# ============================================================
# SPHERE
# ============================================================

elif choice == 11:

    r = get_positive_number("Enter radius: ")

    volume = (4 * math.pi * r * r * r) / 3
    surface_area = 4 * math.pi * r * r

    print("Shape = Sphere")
    print("Volume =", volume)
    print("Surface Area =", surface_area)

    history.append(("Sphere", volume))


# ==========================================================
# HEMISPHERE
# ============================================================

elif choice == 12:

    r = get_positive_number("Enter radius: ")

    volume = (2 * math.pi * r * r * r) / 3
    curved_area = 2 * math.pi * r * r

    print("Shape = Hemisphere")
    print("Volume =", volume)
    print("Curved Surface Area =", curved_area)

    history.append(("Hemisphere", volume))


# ============================================================
# SELECTED SHAPE AND FORMULA
# ==========================================================

print("========================================")

selected_shape = shapes[choice - 1]

print("Selected Shape:", selected_shape)
print("Formula:", formulas[selected_shape])

print("========================================")


# ============================================================
# RANDOM NUMBER
# ============================================================

random_number = random.randint(1, 100)

print("Random Number:", random_number)


# ============================================================
# TOTAL SHAPES
# ===========================================================

print("Total Shapes:", len(shape_set))


# ============================================================
# CALCULATION HISTORY
# ==========================================================

print("Calculation History:")

if len(history) > 0:
    print(history)
else:
    print("No calculation was completed")


# =======================================================
# END PROGRAM
# ==========================================================

print("========================================")
print("Thank you for using the calculator")
print("========================================")
