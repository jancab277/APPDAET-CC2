# APPDAET - Coding Challenge 02
# Challenge 1: Two-Point Linear Equation Analyzer

import math

# Get the coordinates of the first point
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

# Get the coordinates of the second point
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate the changes in x and y
delta_x = x2 - x1
delta_y = y2 - y1

# Calculate the slope
slope = delta_y / delta_x

# Calculate the y-intercept
y_intercept = y1 - slope * x1

# Calculate the x-intercept
x_intercept = -y_intercept / slope

# Calculate the midpoint
midpoint_x = (x1 + x2) / 2
midpoint_y = (y1 + y2) / 2

# Calculate the distance
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Display the results
print("\n===== TWO-POINT LINEAR EQUATION ANALYZER =====")

print(f"Point 1: ({x1}, {y1})")
print(f"Point 2: ({x2}, {y2})")

print(f"\nChange in x (Δx): {delta_x}")
print(f"Change in y (Δy): {delta_y}")
print(f"Slope (m): {slope:.2f}")

print(f"X-intercept: ({x_intercept:.2f}, 0)")
print(f"Y-intercept: (0, {y_intercept:.2f})")

# Slope-intercept form
print(f"Slope-intercept form: y = {slope:.2f}x + {y_intercept:.2f}")

# Point-slope form
print(f"Point-slope form: y - {y1} = {slope:.2f}(x - {x1})")

# General form: Ax + By + C = 0
A = -slope
B = 1
C = -y_intercept

print(f"General form: {A:.2f}x + {B}y + {C:.2f} = 0")

# Midpoint
print(f"Midpoint: ({midpoint_x:.2f}, {midpoint_y:.2f})")

# Distance
print(f"Distance: {distance:.2f}")
