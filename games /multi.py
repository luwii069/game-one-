#multi level inheritance ...when one child class inherits another 
class Organism:
    alive=True

class Animal(Organism):
    def eat(self):
        print("This animal eats ")

class Dog(Animal):
    def bark(self):
        print("This dog is barking")


dog=Dog()
print(dog.alive)
dog.eat()      
dog.bark()
#just like a family tree 



