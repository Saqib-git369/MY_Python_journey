import math

print("--- Quadratic Equation Root Finder (ax² + bx + c = 0) ---")

# Changed to float to support decimal inputs
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# Critical check: 'a' cannot be zero in a quadratic equation
if a == 0:
    print("Error: 'a' cannot be 0. This is not a quadratic equation.")
else:
    # Step 1: Calculate the discriminant
    discriminant = b**2 - 4*a*c
    print(f"\nDiscriminant: {discriminant}")

    # Step 2: Discriminant > 0 (Real and Different)
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print("The roots are real and different.")
        print(f"Root 1: {root1}")
        print(f"Root 2: {root2}")

    # Step 3: Discriminant == 0 (Real and Equal)
    elif discriminant == 0:
        root = -b / (2*a)
        print("The roots are real and equal.")
        print(f"Root: {root}")

    # Step 4: Discriminant < 0 (Complex and Different)
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        print("The roots are complex and different.")
        print(f"Root 1: {real_part} + {imaginary_part}i")
        print(f"Root 2: {real_part} - {imaginary_part}i")