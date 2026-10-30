RootFinder
In this project, we will learn how to find the roots of a Quadratic Equation ((ax^2 + bx + c = 0)) using Python.

How it Works
Step 1: Calculate the Discriminant
We first find the discriminant to determine the nature of the roots: discriminant = b^2 - 4ac

Step 2: Distinct Real Roots
If discriminant > 0, the roots are real and different. They are calculated under the if condition using: x1 = (-b + math.sqrt(discriminant))/(2a) x1 = (-b - math.sqrt(discriminant))/(2a)

Step 3: Equal Real Roots
If discriminant == 0, the roots are real and equal. They are calculated under the first elif condition using: x1=x2= -b/(2*a)

Step 4: Complex Roots
If discriminant < 0, the roots are complex and different. They are calculated under the else condition by separating the real and imaginary parts: x1={real_part} + {imaginary_part}i x2={real_part} - {imaginary_part}i