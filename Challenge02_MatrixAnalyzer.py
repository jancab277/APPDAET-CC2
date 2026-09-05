"""
Coding Challenge 02 - Challenge 2: 3x3 Matrix Analyzer
APPDAET - Week 2 Group Coding Challenge
"""


# Step 1: Collect User Input
print("=" * 45)
print("        3 x 3 MATRIX ANALYZER")
print("=" * 45)
print()

a11 = float(input("Enter a11: "))
a12 = float(input("Enter a12: "))
a13 = float(input("Enter a13: "))

a21 = float(input("Enter a21: "))
a22 = float(input("Enter a22: "))
a23 = float(input("Enter a23: "))

a31 = float(input("Enter a31: "))
a32 = float(input("Enter a32: "))
a33 = float(input("Enter a33: "))


#Perform Matrix Calculations

# Determinant: det(A) = a(ei - fh) - b(di - fg) + c(dh - eg)
determinant = (
    a11 * (a22 * a33 - a23 * a32)
    - a12 * (a21 * a33 - a23 * a31)
    + a13 * (a21 * a32 - a22 * a31)
)

# Trace: sum of the main diagonal
trace = a11 + a22 + a33

# Transpose: rows become columns
t11, t12, t13 = a11, a21, a31
t21, t22, t23 = a12, a22, a32
t31, t32, t33 = a13, a23, a33


# Display Results

print()
print("ORIGINAL MATRIX")
print(f"|  {a11:.2f}  {a12:.2f}  {a13:.2f} |")
print(f"|  {a21:.2f}  {a22:.2f}  {a23:.2f} |")
print(f"|  {a31:.2f}  {a32:.2f}  {a33:.2f} |")

print()
print("MATRIX PROPERTIES")
print(f"Determinant: {determinant:.2f}")
print(f"Trace:       {trace:.2f}")

print()
print("TRANSPOSE")
print(f"|  {t11:.2f}  {t12:.2f}  {t13:.2f} |")
print(f"|  {t21:.2f}  {t22:.2f}  {t23:.2f} |")
print(f"|  {t31:.2f}  {t32:.2f}  {t33:.2f} |")
print("=" * 45)