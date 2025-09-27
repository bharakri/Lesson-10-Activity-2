number = int(input("Enter a number: "))
sum = 0
answer = 0
number1 = number

while number>0:
    remainder = number % 10
    answer = remainder**3
    sum+= answer
    number = number//10
if sum == number1:
    print("This is an Armstrong Number")
else:
     print("This isn't an Armstrong number")
