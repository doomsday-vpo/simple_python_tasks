import math

# Function to calculate the area of a square
def square_area(side):
    return side * side

# Function to calculate the area of a rectangle
def rectangle_area(length, width):
    return length * width

# Function to calculate the area of a circle
def circle_area(radius):
    return math.pi * radius ** 2

# Function to calculate the area of a triangle
def triangle_area(base, height):
    return 0.5 * base * height

# Read the type of geometric figure
figure_type = input("Enter the type of geometric figure: ")

# Calculate the area based on the type of figure
if figure_type == "square":
    side = float(input("Enter the length of the side: "))
    area = square_area(side)
elif figure_type == "rectangle":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = rectangle_area(length, width)
elif figure_type == "circle":
    radius = float(input("Enter the radius of the circle: "))
    area = circle_area(radius)
elif figure_type == "triangle":
    base = float(input("Enter the length of the base of the triangle: "))
    height = float(input("Enter the height of the triangle: "))
    area = triangle_area(base, height)
else:
    print("Invalid figure type!")
    area = None

# Print the calculated area rounded to 3 decimal places
if area is not None:
    print("The area of the", figure_type, "is:", round(area, 3))


