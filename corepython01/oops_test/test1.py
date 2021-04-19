from oops.MyClasses import *

obj1 = Class1() # Object declare and initialize
print(obj1)
print(type(obj1))
print(id(obj1))
print(isinstance(obj1, Class1))

obj2 = Class2()
obj3 = Class2()
print(obj2)
print(type(obj2))
print(id(obj2))
print(isinstance(obj2, Class2))
print(obj2.id, obj2.name, obj2.address)

# Accessing class variable
print(obj2.id)
print(obj2.name)
print(obj2.address)
print()

# changing the value doesnt affect the value of the class value
obj3.id = 2
obj3.name = "Shudhanshu Dwiwedi"
obj3.address = "kathmandu, Nepal"
print(obj3.id)
print(obj3.name)
print(obj3.address)
print()
# Update value
obj2.id = 2
obj2.name = "Shudhanshu Dwiwedi"
obj2.address = "kathmandu, Nepal"

print(obj2.id)
print(obj2.name)
print(obj2.address)

obj4 = Class3()
obj4.f1()
obj4.f2(5, 6)
print(obj4.f3())
print(obj4.f4(30, 40))

# Constructor - Accessing instance variable
obj5 = Class4()
print(obj5.id)
print(obj5.name)
print(obj5.address)
print("-----------------")
# Updating values
obj5.id = 2
obj5.name = "Shudhanshu Dwiwedi"
obj5.address = "Bhaktpur"
print(obj5.id)
print(obj5.name)
print(obj5.address)
print(obj5) # call __str__() method
print("___________")
obj6 = Class5(1,"Aanshu Dwiwedi","Lalitpur")
print(obj6)

print("------------")
obj7 = Class6(100)
print(obj7.getId())
print(obj7)
obj7.setId(102)
print(obj7.getId())
print(obj7)

print("____________")
obj8 = Class7() #Class7() -> __init__(self, id=0)
print(obj8)
print("-------------")
obj8_1 = Class7(2) #Class7() -> __init__(self, id=0)
print(obj8_1)
print("------------")

obj9 = Class8(1, "Aanshu") # Object declare and initialize
#print(obj9.id) # AttributeError: 'Class8' object has no attribute 'id'
print(obj9.getId(), obj9.fullName)
print(obj9)
print("------------")