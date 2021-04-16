from my_libs import MyFunctions # import Python file

MyFunctions.f1() # call the function
"""
for i in range(10):
    MyFunctions.f1()
"""
# single line comment

"""
multi-line comments
"""
"""
num1 = 3 + 5

MyFunctions.f2(num1)
"""
"""
# f3(num1, num2) # function signature - function name and list of parameter(s)
n1 = 9
n2 = 8
MyFunctions.f3(n1, n2)

n1 = 90
n2 = 81
MyFunctions.f3(n1, n2)


n1 = float(input("Enter first number :"))
n2 = float(input("Enter second number: "))
MyFunctions.f3(n1, n2)
num1 = MyFunctions.f4()
print(num1)
"""
var1 = MyFunctions.f5()
print(var1)

num1 = MyFunctions.f6(10, 12)
print(num1)

