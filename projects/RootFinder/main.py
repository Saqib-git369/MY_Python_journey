
import math
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))

discriminant=b**2-4*a*c

if discriminant>0:
    root1=(-b+math.sqrt(discriminant))/(2*a)
    root2=(-b-math.sqrt(discriminant))/(2*a)
    print("The roots are real and different.")
    print("Root 1:", root1)
    print("Root 2:", root2)
elif discriminant==0:
    root=(-b)/(2*a)
    print("The roots are real and equal")
    print("Root:", root)
elif discriminant<0:
    real_part=-b/(2*a)
    imaginary_part=math.sqrt(-discriminant)/(2*a)
    print("The roots are different and complex")
    print("root1:", real_part, "+", imaginary_part, "i")
    print("root2:", real_part, "-", imaginary_part, "i")
