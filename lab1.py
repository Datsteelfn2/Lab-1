# Program Name: Lab1.py
# Course: IT1114/Section 1
# Student Name: Elhadj Diallo
# Assignment Number: Lab1
# Due Date: 8/31/ 2025
# Purpose:The purpose of the program is to calculate the amount and cost of purchasing flooring. As students this labs reinforces 
# What we learned about variables, converting inputs to datatypes and combining math into the our programs.

# List specific resources used to complete the assignment.| The odin project- used to learn how to use git and github
length=int(input("What is the length:>"))
width=int(input("What is the width:> "))
cost=float(input("What is the cost of the flooring per square foot:> "))
square_feet=length*width

flooring=length*width*cost
tax=flooring*.07
total=flooring+tax
print(f"The square feet is {square_feet}")
print(f"The flooring is {flooring}")
print(f"Tax{tax}")
print(f"Total:{total}")