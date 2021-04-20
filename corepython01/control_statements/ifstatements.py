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
num1 = 6
if (num1 == 0):
    print("ZERO")
elif (num1 == 1):
    print("ONE")
elif (num1 == 2):
    print("TWO")
else:
    print("OTHER")

# Nested if
"""
Syntax 
if (condition1):
    if (condition2):
        Statement for true
"""
# Example
num1 = 9
num2 = 8
num3 = 4
if(num1>num2):
    if(num1>num3):
        print(num1)

# if statement with logical operator
"""
if(condition1 logical_operator condition2)
    Statement for true
    
Note:
- AND, OR
"""

num1 = 9
num2 = 8
num3 = 4
if((num1>num2) and (num1>num3)):
    print(num1)
elif((num2>num1) and (num2>num3)):
    print(num2)
else:
    print(num3)

# Looping statements

count = 1
while(count<=10):
    print("Aanshu Dwiwedi")
    count+=1

# Tasks
"""
    1. Print 1 to 10
    2. Print first no to last no
    3. Print sum of 1 to 10
    4. Print average of 1 to 10
    5. Print factorial of 1 to 10
    6. Print odd numbers between 1 to 10
    7. Print even numbers between 1 to 10
    8. Print sum of odd numbers between 1 to 10
    9. Print sum of even numbers between 1 to 10 
    Using While loop only For this
"""

# For Loop
for i in range(5): # 0 to 4
    print(i)
print("---------")
for i in range(1, 6): # 1 to 5
    print(i)
print()
for i in range(1, 21, 2): # 1,3,5,7,....<21
    print(i)

print("-------------------------")

#nested Loop
for i in range(5):
    for j in range(5):
        print(i*j)
    print()
print()

# break and continue
# break
print("-----------------")
for i in range(10):
    if i == 5:
        break
    print(i)
print("---------------")

# continue
for i in range(10):
    if i == 5:
        continue
    else:
        print(i)
print("--------------")
# Pass
class c1:
    pass

# return
def f1():
    return "hello"

# range()
print(range(10))
var1 = range(10)
print(var1)