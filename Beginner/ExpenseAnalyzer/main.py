"""This is the project where we learn about some in built
 functions like sum(),len(),max(),min() etc. 
and basically it extrcts some data from  traveling expenses """




food=  float(input("Enter the food expense: $"))
travelling= float(input("Enter the travelling expense: $"))
shopping= float(input("Enter the shopping expense: $"))
bills= float(input("Enter the bills expense: $"))

Expenses= [food, travelling, shopping, bills]

total= sum(Expenses)
average= total/len(Expenses)
maximum= max(Expenses)
minimum= min(Expenses)


print(total, "is the total expense")
print(average, "is the average expense")
print(maximum, "is the maximum expense")
print(minimum, "is the minimum expense")







