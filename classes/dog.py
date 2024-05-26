# Dylan Nelson
# May 13, 2024
# dog.py

class Dog:
    '''
    Used to model the behavior of a dog.\n
    Methods: bark, sit, dog_years.
    '''
    def __init__(self, name, age):
        '''initiliazes the instance of a dog, requiring a name and an age.'''
        self.name = name
        self.age = age

    def bark(self):
        '''Simulates a dog barking.'''
        print(f'{self.name} just barked!')
    
    def sit(self):
        '''Simulates a dog reacting to a "Sit" command.'''
        print(f'{self.name} sat down.')

    def dog_years(self):
        '''Reports back the dog's age in dog years.'''
        # Because multiplication is being performed, the int class is called 
        # to convert any strings into integers
        print(f'{self.name} is {self.age} years old, '
              f'{int(self.age) * 7} in dog years.')

# Creates multiple instances of the Dog class
my_dog = Dog('Willie', '6')
your_dog = Dog('Jerome', 4)

# After creating "my_dog" we can use the variables that are associated.
print(f"My dog's name {my_dog.name}. He is {my_dog.age} years old.")

# Call forth the methods within the Dog class, both methods shown can be
# successfully used however the latter is the conventional method.
Dog.bark(my_dog)
my_dog.sit()
my_dog.dog_years()
your_dog.bark()
your_dog.sit()
your_dog.dog_years()

# Written out in long form this is what the above example looks like, it is 
# easier to condense the dog into a single variable
Dog.dog_years(Dog('Mark', 12))
