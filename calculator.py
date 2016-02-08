#! /usr/bin/python

print("1: ADDITION")
print("2: SUBTRACTION")
print("3: MULTIPLICATION")
print("4: DIVISION")

CHOICE = raw_input("Enter the Numbers:")

if CHOICE == "1":
    a = raw_input("Enter the value of a:")
    b = raw_input("Enter the value of b:")
    c = a + b
    print c

elif CHOICE == "2":
    a = raw_input("Enter the value of a:")
    b = raw_input("Enter the value of b:")
    c = a - b
    print c

elif CHOICE == "3":
    a = raw_input("Enter the value of a:")
    b = raw_input("Enter the value of b:")
    c = a * b
    print c

elif CHOICE == "4":
    a = raw_input("Enter the value of a:")
    b = raw_input("Enter the value of b:")
    c = a / b
    print c

else: 
 print "Invalid Number"
 print "\n"


