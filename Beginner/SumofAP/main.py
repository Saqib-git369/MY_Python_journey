#taking first term
a=int(input("Enter the first term of the AP: "))
#taking common difference
d=int(input("Enter the common difference of the AP: "))
#taking number of terms
n=int(input("Enter the number of terms of the AP: "))
#calculating the sum of AP
sum_AP=n*(2*a+(n-1)*d)/2
print("The sum of the AP is: ", sum_AP)