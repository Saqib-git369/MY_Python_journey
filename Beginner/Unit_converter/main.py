print("Option 1: km to miles")
print("Option 2: kg to pounds")
print("Option 3: cm to inches")
print("Option 4: celsius to fahrenheit")

choices = input("Choose the options above: ")

if choices == "1":
    km = float(input("Enter the value in km: "))
    miles = km * 0.621371
    print(km, "km is equal to", miles, "miles")

elif choices == "2":
    kg = float(input("Enter the value in kg: "))
    pounds = kg * 2.20462
    print(kg, "kg is equal to", pounds, "pounds")

elif choices == "3":
    cm = float(input("Enter the value in cm: "))
    inches = cm * 0.393701
    print(cm, "cm is equal to", inches, "inches")

elif choices == "4":
    celsius = float(input("Enter the value in celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(celsius, "celsius is equal to", fahrenheit, "fahrenheit")

else:
    print("Invalid choice. Please select a valid option.")

print("Thank you for using the unit converter!")