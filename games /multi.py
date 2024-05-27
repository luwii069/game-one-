#multi level inheritance ...when one child class inherits another 
class Organism:
    alive=True

class Animal(Organism):
    def eat(self):
        print("This animal eats ")
        return self
#in method chaining we return self 
class Dog(Animal):
    def bark(self):
        print("This dog is barking")
        return self



#method chaining below 
dog=Dog()
dog.eat().bark()
#dog=Dog()
#print(dog.alive)
#dog.eat()      
#dog.bark()
#just like a family tree 

#in multiple inheritance child class is derived from more than one parent class 




