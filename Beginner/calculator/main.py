marks= float(input("Enter the marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
elif marks >= 50:
    grade = "E"
else:
    grade = "F"


if marks >= 40:
    print("Congratulations! you have passed the exam with grade", grade)
else:
    print("You have failed the exam")


print("Your grade is", grade) #this is change from main branch to branch1
