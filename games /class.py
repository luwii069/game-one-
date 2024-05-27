#object oriented programming
class Car:
    #wheels =4 #class variable...remains constant in every object 
    
    #constructor
    def __init__(self,make,model,year,color):
         self.make=make    #these are instance variables 
         self.model= model
         self.year = year
         self.color=color 
    def drive(self):
        print (" this car is driving ")
    def stop(self) :
        print("this car has stopped ") 


car_1=Car("mercedes","c63",2021,"red")
print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color) 

car_1.drive()
car_1.stop()
#all the cars will now display ....the above is typically just classes in python 
#diff between an instance variable and a class variable is 
#instance variables are declared inside the constructor and can be 
#changed while class variables are declared outside and they remain as constants 