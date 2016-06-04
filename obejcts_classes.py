import os
import sys

class Animal:
    __name=""
    __height = 0
    __weight = 0
    __sound = 0
    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height= height
        self.__weight= weight
        self.__sound = sound

    def set_name(self, name):
        self.__name = name
    def set_height(self,height):
        self.__height = height
    def set_weight(self,weight):
        self.__weight = weight
    def set_sound(self, sound):
        self.__sound = sound

    def get_name(self):
        return self.__name
    def get_height(self):
        return self.__height
    def get_weight(self):
        return self.__weight

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and kilograms and says {}".format(self.__name,
                                                                    self.__height,
                                                                    self.__weight,
                                                                    self.__sound)
cat= Animal('kitty',20,10,'Meow')
print (cat.toString())

class dog(Animal):
    __owner=""

    def __init__(self,name, height, weight ,sound,owner):
        self.__owner = owner
        super(dog,self).__init__(name,height,weight,sound)

    def set_owner(self,owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_type(self):
        print("dog")

    def toString(self):
        return "{} is {} cm tall and kilograms and says {} his owner is {}".format(self.__name,
                                                                                   self.__height,
                                                                                   self.__weight,
                                                                                   self.__sound,
                                                                                   self.__owner)

    def multiple_sounds(self, how_many= None):
        if how_many is  None:
            print(self.get_sound())
        else:
            print(self.get_sound()*how_many)

spot = dog("Spot",53,27,"Ruff","Derek")
print(spot.toString())
#POLIMORFISOM

class AnimalTesting:

    def get_type(self, animal):
        animal.get_type()
test_animals = AnimalTesting()
test_animals.get_type(cat)
test_animals.get_type(spot)

spot.multiple_sounds(4)
spot.multiple_sounds()

