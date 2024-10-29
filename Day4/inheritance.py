class Animal():
    def sound(self):
        print("All animal has a sound")

class Dog(Animal):
    def bark(self):
        print('Dog barks')

class Cat(Animal):
    def meow(self):
        print("Cat says Meow")

d = Dog()
c = Cat()

d.sound()
d.bark()
c.sound()
c.meow()

for x in (d,c):
    print(x.sound())

