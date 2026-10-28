from random import choice

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




