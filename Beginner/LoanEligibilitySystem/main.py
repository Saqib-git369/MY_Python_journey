age= float(input("Enter your correct age: "))
salary= float(input("Enter your correct salary: "))
credit_score= float(input("Enter your correct credit score: "))
existing_loan= input("Do you have any existing loan? (yes/no): ")

if age>=18 and salary>=30000 and credit_score>=700 and existing_loan=="no":
    print("Congratulations! You are eligible for the loan.")
else:
    print("Sorry! You are not eligible for the loan.")
    
        