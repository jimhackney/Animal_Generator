#The Animal class defines an animal and its attributes
import random

class Animals:
    #define and assign attributes
    def __init__(self, animal_type, name):
        self.__animal_type = animal_type
        self.__name = name
        
    def get_animal_type(self):
        return self.__animal_type

    def get_name(self):
        return self.__name    

    def check_mood(self):
        number = random.randint(1, 3)
        if number == 1:            
            self.__mood = 'happy'
        elif number == 2:
            self.__mood = 'hungry'
        elif number == 3:
            self.__mood = 'sleepy'

        return self.__mood
            
        
    
