#class inheritence 
class Animal:
    alive = True 
    def eat(self):
        print("This animal is eating ")
    def sleep(self):
        print("This animal is sleeping ")
#pass the ain class name as a parameter to the preceeding
class Rabbit(Animal):
    pass
class Fish(Animal):
    pass
class Hawk(Animal):
    pass

rabbit=Rabbit()
fish=Fish()
hawk=Hawk()

print(rabbit.alive)
fish.eat()



