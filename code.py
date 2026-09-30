1. Basic inheritance

class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


dog = Dog()

dog.speak()
dog.bark()
What happens here?

Animal is the parent class.

class Animal:

Dog is the child class:

class Dog(Animal):

Because Dog inherits from Animal, a Dog object can use methods from Animal.

So:

dog.speak()

works even though speak() isn't written inside Dog.
  

2. What is super()?

super() lets the child class access functionality from its parent class.

class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


dog = Dog("Bruno", "Labrador")

print(dog.name)
print(dog.breed)

Here:

super().__init__(name)

calls the parent's:

Animal.__init__()

So the parent takes care of:

self.name = name

while the child adds:
