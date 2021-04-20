# if statement
"""
syntax

if(condition):
    statement for true

# Condition
    value relational_operator value
    # ==, !=, > , <, >=, <=
    # result -> True or False
"""
# Example
num1 = 1 # initialize /store
if(num1 == 0): # compare equals to ; value of num1 is equals to zero
    print("ZERO")
print("END")
"""
# if else
Syntax
if (Condition):
    Statement for True
else:
    Statement for False
        
"""

num1 = 1
if(num1==0):
    print("Zero")
else:
    print("Others")
"""
# if ... elif statement
Synatx
if (condition1):
    Statement for True
elif (condition2):
    Statement for True
elif (condition3):
    Statement for True   
else:
Statement for False
"""
num1 = 2
if (num1 == 0):
    print("ZERO")
elif (num1 == 1):
    print("ONE")
elif (num1 == 2):
    print("TWO")
else:
    print("OTHER")
