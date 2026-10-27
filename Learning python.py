import keyword
import sys

print ("Hello world")
#arithmatic Operates

a = 10
b = 20

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

#assignment Operates

a = 45

a = a + 6
print(a)

a = 45
a  -= 85
print(a)

a = 45
a = a * 85
print(a)

a = 45
a *= 3
print(a)


a = 45
a /= 85
print(a)


print(keyword.kwlist) # to know what atr the keywords
print(len(keyword.kwlist))  #length of the key word
print (keyword.iskeyword("Hi")) # To know this is a keyword are not

print (keyword.iskeyword("if"))






K = 10
print(sys.getsizeof(K))




import sys
name ="raja"
print(sys.getsizeof(name))


name = input("Enter your name: ")
print(name)

#tycasting

a = input("print enter first number : ")
b = input (" print enter second number : ")

c = a + b

a = int input()
b = int(b)
print()