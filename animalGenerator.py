#This program manages animals
import animals

#define main function
def main():
    print('Welcome to the animal generator!')
    print('This program creates Animal objects.')
    print()

    #Call make_list function and assign it to
    #animals variable
    animals = make_list()    

    #Call the display_list
    display_list(animals)
    
                        
#The make_list function gets data from the user.
#The function returns a list of animal objects
#containing the data
def make_list():
    #Create an empty list
    animals_list = []

    #another animal?
    another = 'y'

    while another == 'y':
        #Get animal type
        animal_type = input('What type of animal would you ' +
                                   'like to create? ')
        #Get animal name
        name = input('What is the animal’s name? ')
        print()

        #Create Animal object and assign it to the
        #animal_obj variable
        animal_obj = animals.Animals(animal_type, name)
        
        #Add animal object to dictionary
        animals_list.append(animal_obj)        

        #another animal?
        another = input('Would you like to add more animals (y/n)? ')
        print()
    #return the list
    return animals_list

#The display_list fucntion accepts a list containing
#Animal objects as an argument and displays the
#data stored in each object
def display_list(animals_list):
    print('Animal List:')
    for item in animals_list:
        print(item.get_animal_type(), 'the', item.get_name(), \
              'is', item.check_mood())

#Call the main function
main()
        
        

    

    
