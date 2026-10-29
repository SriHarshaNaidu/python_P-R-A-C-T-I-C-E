from random import choice
from tarfile import GNU_FORMAT
from unittest import case

age = int(input("enter the age : "))
if age >= 20 :
    print("you are not  eligible  for job ")
elif age <= 20 :
    print("you are eligible for job ")
else:
    print("you have to wait for next year")

num = int(input("Enter a number: "))

if num > 0:
     print("The number is positive")
elif num < 0:
        print("The number is negative")
else:
        print("The number is zero")


###let me run in grade  format
marks = int(input("Enter student marks :"))

if marks >= 95 :
    print("First Class")
elif marks >= 75 :
    print("second Class")
elif marks >= 40 :
    print("third Class")
elif marks >= 35 :
    print ("Just Pass")
else :
    print ("Fail")


## match case

print ("1 . kill the man ")
print ("2 . kill the dog ")
print ("3 . kill the cat ")
print ("4 . kill the rat ")

choice = int(input("enter your choice :"))

match choice :
    case 1 :
        print("kill the man ")
    case 2 :
        print("kill the dog ")
    case 3 :
        print("kill the cat ")
    case 4 :
        print("kill the rat ")
    case _ :
        print("invalid")



# loop
#forloop


name = "harsha"
for A in name :
    print(A)

cartprices = [400, 500, 5000, 25000]
for total in cartprices :
    print(total)

cart_prices = [400, 500, 5000, 25000]
total = 0
for total_price in cart_prices :
    total += total_price
    print(total)


House_rent = [5000, 25000, 45000, 75000]
total = 0
for Total_rents in House_rent :
    total += Total_rents
    print (total)

salary = [5000, 25000, 85000, 300, 65000]
biggest = salary[0]
for num in salary :
 if num > biggest :
      biggest = num
print (biggest)


salary = [5000, 25000, 85000, 300, 65000]
smallest = salary [0]

for num in salary :
    if num < smallest :
        smallest = num

print (smallest)

#sum
salary = [5000, 25000, 85000, 300, 65000]
total = 0
for num in salary :
total = total + num
print (total)


#whiled loop
count = 5
while count <= 10:
   print (count)
   count = count + 2

count = 3
while count <= 10:
    print (count)
    count = count + 3

count = 2
while count <= 10 :
    print (count)
    count = count + 4

count = 8
while count >= 6:
    print (count)
    count = count / 2

count = 15
while count >=5 :
    print (count)
    count = count + 1


students = [
    {"Name" : "harsha" , "marks" : 95 },
    { "Name" : "ravi" , "marks" : 70 },
    {"Name" : "jeva" , "marks" : 30 },
    {"Name" : "ravai" , "marks" : 45 },

]
for student in students:
    if student["marks"] <= 35 :
         continue

        print ("certificate send to : ", student["Name"])


 for i in  range(1, 11):
     if i == 5 :
         continue

      print (i)



for H in range (1, 15) :
    if H == 10:
        break
     print (H)

#Skip numbers divisible by 3 using continue
for Y in range (1 , 10) :
    if Y % 3 == 0:
        continue
    print (Y)


#
# The first question is: write a program that takes a number and prints whether it is positive, negative, or zero using if, elif, and else

num = int(input("enter a number : "))
if num > 0 :
     print(" the number is positive")
elif num < 0 :
     print ("the number is negative")
else:
     print (" the number is zero")


#Write a program to check whether a student passed or failed.

students = [
    {"name" : "ravi" , "marks": 50},
    {"name" : "raju" , "marks" : 65},
    {"name": "priya", "marks": 90},
    {"name": "arun", "marks": 30},
    {"name": "hari", "marks": 20},
    {"name": "rupesh", "marks": 50},
]
for student in students :

    if student[ "marks"] >= 35:
         print( student["name"] ," pased ")
    else :
       print ( student["name"] ," failed ")

# numbers from 1 to 100 using a for loop. Want to try writing that next, step by step, like we just did?

for h in range (1, 100):
    print ( h )

#Print numbers from 100 down to 1 using a while loop.

num = 100
while num >= 1:
    print(num)
    num = num -1



#Find the sum of numbers from 1 to 100.

sum = 0
for num in range (1, 101):
    sum = sum + num
print ("total ; ", sum)


# Find a student in a list. I
students = [ "priyanka" , "harsha" , "ravi", "raju" ]
name = "priyanka"
if name in students :
    print ("student found")
else :
    print ( "student not found")

#
students = [ "priyanka" , "harsha" , "ravi", "raju" ]
name = "suresh"
if name in students:
    print ("student found")
else :
    print ("student not found")


# Create a calculator using match case.
num1 = float(input("enter first number : "))
num2 = float (input("enter second number: "))

op = input(" enter operator (+, -, *, /, %, //): ")

match op :
    case "+" :
        print ("result : ", num1 + num2)
    case "-" :
        print ( "result :" , num1 - num2)
    case "*" :
        print ( "result :" , num1 * num2)
    case "/" :
        print ( "result :" , num1 / num2)
        if num2 != 0:
          print("result :", num2 / num1)
        else:
         print("Cannot divide by zero")
    case _:
         print ("invaled operator")

# Write a program to print all even numbers from 1 to 50.
for N in range (1, 51):
    if N % 2 == 0:
        print(N)
#Write a program to stop searching when a particular product is found using break.
products = ["laptop", "mobile", "tablet", "keyboard"]
target = input("enter target : ")
for product in products :
    if product == target:
       print("product found :" , product)
       break
    else :
        print ("product not found")

products = ["Fan", "light", "specker", "Gun"]
target = "Gun"
for product in products :
    if product == target:
        print("product found :" , product)
        break











