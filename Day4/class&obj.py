# Class 
class MyClass:
    def config():
        pass

# Object 
obj = MyClass()
print(type(obj))

# __init__ is constructor - invoked on object creation 
class sClass:
    def __init__(self,Name,age) -> None:
        self.name = Name
        self.age = age

    def show(self):
        print(self.name + " is my name & my age is " , self.age)

obj1 = sClass("Hari", 30)
obj1.show()

obj1.age = 35 #updating 
obj1.show()

del obj1.age #deleting

del obj1 #deleting the object itself

