#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      anshi
#
# Created:     19-02-2022
# Copyright:   (c) anshi 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#                 MINI PROJECT IN PYTHON

# Let's build a Mini Calculator by using Python

first = input("Enter first number: ")
operator = input("Enter operator (+ - * / %): " )
second = input("Enter second number: ")

#Now we convert fist and second variable which is string into int
first = int(first)
second = int(second)

if operator == "+":
    print(first + second)

elif operator == "-":
    print(first - second)   #agr upar k condition false hai then ye check kro otherwise agr ye condition v false hai then niche k condition check kro.
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first - second)
elif operator == "%":
    print(first % second)
#we can write elif again n again becoz if the above condition false after that the next elif will be checked and executed . if we write "if" again and again then all the conditions will be checked

else:
    print("Invalid operation")

