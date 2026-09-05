# ==============================================================================
# COURSE: APPDAET
# ACTIVITY: Coding Challenge 02
# GROUP NAME: APPDAET_BTIS1_20261 - Full Groupings 3
# PROGRAM: Challenge 1 - Two-Point Linear Equation Analyzer
# PURPOSE: Accepts two Cartesian points and calculates slope, intercepts, 
#          equation forms, midpoint, and distance without external libraries.
# ==============================================================================

# Header output display
print("==================================================")
print("     CHALLENGE 1: TWO-POINT LINE ANALYZER")
print("==================================================")

# Step 1: User Input
print("\nEnter Point 1 coordinates:")
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))

print("\nEnter Point 2 coordinates:")
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Step 2: Basic Calculations
delta_x = x2 - x1
delta_y = y2 - y1

# Slope
slope = delta_y / delta_x

# Intercepts
y_intercept = y1 - (slope * x1)
x_intercept = -y_intercept / slope

# Midpoint
mid_x = (x1 + x2) / 2
mid_y = (y1 + y2) / 2

# Distance using basic exponentiation (x ** 0.5 is square root)
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# General Form Coefficients (Ax + By + C = 0)
A = slope
B = -1.0
C = y_intercept

# Step 3: Output Results
print("\n==================================================")
print("               ANALYSIS RESULTS")
print("==================================================")
print("Change in x (Δx)       :", delta_x)
print("Change in y (Δy)       :", delta_y)
print("Slope (m)              :", slope)
print("X-intercept            : (" + str(x_intercept) + ", 0)")
print("Y-intercept            : (0, " + str(y_intercept) + ")")
print("--------------------------------------------------")
print("Slope-intercept form   : y = " + str(slope) + "x + " + str(y_intercept))
print("Point-slope form       : y - " + str(y1) + " = " + str(slope) + "(x - " + str(x1) + ")")
print("General form           : " + str(A) + "x + (" + str(B) + ")y + (" + str(C) + ") = 0")
print("--------------------------------------------------")
print("Midpoint               : (" + str(mid_x) + ", " + str(mid_y) + ")")
print("Distance               : " + str(distance))
print("==================================================")