
# Dylan Nelson
# May 14, 2024
# car.py

'''Contains the Classes to represent a Car, ElectricCar, and a Battery.'''

class Car:
    '''A model of a car.\n
    Methods: get_descriptive_name.'''

    def __init__(self, make, model, year,):
        '''Intializes an instance of a car with the following attributes:\n
        make, model, year'''
        self.make = make
        self.model = model
        self.year = year
        # "self_odometer is set to a default value of 0 here. to override this
        # a value for odometer will need to be passed in to the class when the 
        # instance is first created."
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '''Returns the full name of the car with all of the descriptors.'''
        long_name = (f'{self.year} {self.make} {self.model}')
        return long_name.title()
    
    def read_odometer(self):
        '''Returns the odometer reading.'''
        odometer = (f'The vehice has {self.odometer_reading} miles.')
        return odometer
    
    def update_odometer(self, mileage):
        '''Updates the value of the odometer.'''
        print(f'Updating odometer to {mileage} miles...')
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            print('Done.')
            if mileage > 1000000:
                print("This doesn't seem like a new car...")
        else:
            print('Rolling back the odometer is not allowed.')

    def increment_odometer(self, miles):
        '''Increments the curent value of the odometer.'''
        print(f'Incrementing {miles} miles to the odometer.')
        if miles > 0:
            self.odometer_reading += miles
            print('Done.')
        else:
            print('Please provide a number greater than 0.')

class ElectricCar(Car):
    '''Represent the aspects of a car, specific to electric vehicles.'''

    def __init__(self, make, model, year):
        '''Initialize the attributes of the parent class from "Car".'''
        # "super()" is a special function that allows for the attributes from 
        # the original "Car" class to be transfered over completely to the 
        # child class. The name derives from superclass/subclass convention.
        super().__init__(make, model, year)
        self.battery = Battery()

class Battery:
    '''Represents the battery that is present in an electric car.'''

    def __init__(self, battery_size=40):
        '''Initializes an instance of a battery with the following attributes:
        \nSize.'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''Print a statement that describes the size of the car's battery.'''
        print(f'The battery is {self.battery_size}-kWh.')
    
    def get_range(self):
        '''Gives the estimated range that the battery will allow the user to 
        drive in miles.'''
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 200
        print(f'This vehicle will go for about {range} miles '
                  'before needing a recharge.')
        
    def upgrade_battery(self):
        '''Upgrades the battery size to be 65'''
        if self.battery_size < 65:
            self.battery_size = 65
