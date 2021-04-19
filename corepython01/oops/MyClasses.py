class Class1():
    pass
    # class variables
    # constructors
        # instance variables
    # functions

class Class2():
    # class variables
    id = 1
    name = "Aanshu Dwiwedi"
    address = "Lalitpur, Nepal"

    # Member function
    def __str__(self):
        #return (str(id)+", "+name+", "+address)
        return ("Hello from __str__()")



class Class3():
    def f1(self):
        print("Hello from f1()")

    def f2(self, num1, num2):
        num3 = num1 + num2
        print("Result : ", num3)

    def f3(self):
        return (30+40)

    def f4(self, num1, num2):
        return (num1+num2)

class Class4():
    # initialize function - Constructor
    def __init__(self):
        # instance variables
        self.id = 1
        self.name = "Aanshu Dwiwedi"
        self.address = "Lalitpur"

    def __str__(self):
        return str(self.id)+", "+self.name+", "+self.address

class Class5():
    # initialize function - Constructor
    def __init__(self,id,name,address):
        # instance variables
        self.id = id
        self.name = name
        self.address = address

    def __str__(self):
        return str(self.id)+", "+self.name+", "+self.address

class Class6():
    # initialize function - Constructor
    def __init__(self, id):
        # instance variables
        self.id = id
    # Setter
    def setId(self, id):
        self.id = id


    # Getter
    def getId(self):
        return str(self.id)

    #str
    def __str__(self):
        return str(self.id)

class Class7():
    # initialize function - Constructor
    def __init__(self, id=0): #default value to parameter
        # instance variables
        self.id = id
    # Setter
    def setId(self, id):
        self.id = id


    # Getter
    def getId(self):
        return str(self.id)

    #str
    def __str__(self):
        return str(self.id)

class Class8(Class7): # Inheritance - Class7 ->Super class ; Class8 -> Sub Class
    def __init__(self,id=0, fullName="NA"):
        super().__init__(id) # passing id to Class7 init
        self.fullName=fullName

    def setFullName(self, fullName):
        self.fullName=fullName

    def getFullName(self):
        return self.fullName

    def __str__(self):
        return super(Class8, self).__str__()+", "+self.fullName
