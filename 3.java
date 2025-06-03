
#encapsulation
class Student:
    def init(self,marks):    #default constructor
        self.marks=marks
        self.__marks=marks   #private
    def getter(self):
        return self.__marks
    def setter(self,marks):                  
        self.__marks=marks
s1=Student(79)
#set the data
s1.setter(79)
#get the data
ans=s1.getter()
print(ans)


#abstraction
from abc import ABC,abstractmethod                          
class four_wheeler(ABC):
    @abstractmethod
    def engine():
        return "hello this is process of making car"
class swift(four_wheeler):
    def car_start():
        return"car is moving"
car_1=swift
ans=car_1.car_start()

print(ans)



#INHERITANCE:
#SINGLE INHERITANCE
class father:        #parent class
    def father_method():
        return "This is father method"
#inheriting father class
class child(father);
    def child_method():
        return "This is child method"
parent_object=father
child_object=child
print(parent_object.father_method())
print(child_object.child_method())
print(child_object.father_method())


#MULTIPLE INHERITANCE
class father:        
    def father_method():
        return "This is father method"
class mother:
    def mother_method():
        return "This is mother method"
class child(father,mother):
    def child_method():
        return "I have properties of mother and father"      
father_obj=father
mother_obj=mother
child_obj=child
print(father_obj.father_method())
print(mother_obj.mother_method())
print(child_obj.child_method())
print(child_obj.father_method())
print(child_obj.mother_method())





#multilevel inheritance
class grandfather:        
    def grandfather_method():
        return "This is grandfather method"
class father:        
    def father_method():
        return "This is father method"

class child(grandfather,father):
    def child_method():
        return "I have properties of grand father and father"
grandfather_obj=grandfather        
father_obj=father
child_obj=child
print(grandfather_obj.grandfather_method())
print(father_obj.father_method())
print(child_obj.child_method())
print(child_obj.grandfather_method())
print(child_obj.father_method())



#HIRARCHIAL INHERITANCE
class grandfather:        
    def grandfather_method():
        return "This is grandfather method"
class grandmother:        
    def grandmother_method():
        return "This is grandmother method"
class father:        
    def father_method():
        return "This is father method"

class child(grandfather,grandmother,father):
    def child_method():
        return "I have properties of grand father,grandmother and father"
grandfather_obj=grandfather        
grandmother_obj=grandmother 
father_obj=father
child_obj=child
print(grandfather_obj.grandfather_method())
print(grandmother_obj.grandmother_method())
print(father_obj.father_method())
print(child_obj.child_method())
print(child_obj.grandfather_method())
print(child_obj.grandmother_method())
print(child_obj.father_method())


#HYBRID
class grandfather:        
    def grandfather_method():
        return "This is grandfather method"
class father:        
    def father_method():
        return "This is father method"
class mother:        
    def mother_method():
        return "This is mother method"
class child(grandfather, father,mother):
    def child_method():
        return "I have properties of grand father,mother and father"
grandfather_obj=grandfather        
father_obj=father
mother_obj=mother 
child_obj=child
print(grandfather_obj.grandfather_method())
print(father_obj.father_method())
print(mother_obj.mother_method())
print(child_obj.child_method())
print(child_obj.grandfather_method())
print(child_obj.mother_method())
print(child_obj.father_method())


#POLYMORPHISAM
class Animal:
    def speak():
        return "animal is speaking"
class Bird(Animal):
    def speak():
        return "bird is speaking"
animal_object=Animal
bird_object=Bird 
print(animal_object.speak())
print(bird_object.speak())



SUM OF SQUAE OF ANUMBERS
n=3645
sum=0
while(n>0):
    digit=n%10
    sum=(digit*digit)+sum
    n=n//10
print(sum)

