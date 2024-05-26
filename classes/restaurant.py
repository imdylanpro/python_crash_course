# Dylan Nelson
# May 13, 2024
# restaurant.py

class Restaurant:
    '''Creates an instance of a restaurant.\n
    Methods: describe_restaurant, open_restaurant, close_restaurant.'''

    def __init__(self, restaurant_name, cuisine_type):
        '''Initiliaizes the instance of a restaurant, 
        requiring a name and cuisine.'''
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        '''Describes a restaurant using the given name and cuisine'''
        print(f'We are the {self.name}. We serve {self.cuisine}.')
        
    def open_restaurant(self):
        '''Simulates opening a restaurant.'''
        print(f'{self.name} is now open!')

    def close_restaurant(self):
        '''Simulates closing a restaurant.'''
        print(f'{self.name} is now closed!')

    def set_number_served(self, customers):
        '''Sets the number of people that have been served so far.'''
        self.number_served = customers

    def increment_number_served(self, customers):
        '''Increments the number of people served'''
        self.number_served += customers

class IceCreamStandRestaurant(Restaurant):
    '''Creates an instance of an ice cream stand, using the "Restaurant" class
    as the parent class.'''

    def __init__(self, restaurant_name, cuisine_type):
        '''Initializes an instance of the parent class "Restaurant".\n
        Requires 2 parameters: "name", "cuisine".'''
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']

    def display_flavors(self):
        '''Displays the flavors available in "self.flavors" list'''
        print(f'Our flavors today are: {self.flavors}')

# Store the original classes methods all inside a function for ease of calling 
# and troubleshooting.
def restaurant_methods():
    # Build 3 restaurants using the "Restaurant" class, then using the methods
    # written within.
    my_restaurant = Restaurant("Dylan's Taco Truck", 
                            "Tacos, Churros, Salsa, and Chips",)
    my_restaurant.open_restaurant()
    my_restaurant.describe_restaurant()
    my_restaurant.close_restaurant()

    competition_restaurant = Restaurant("Mark's Taco Van", 
                                        "Tacos, beans, Asada, Guacamole")
    competition_restaurant.open_restaurant()
    competition_restaurant.describe_restaurant()
    competition_restaurant.close_restaurant()

    friends_restaurant = Restaurant("Lane's Ice Cream Shop",
                                    "Hot Fudge Sunday, Shakes, Flurries")
    friends_restaurant.open_restaurant()
    friends_restaurant.describe_restaurant()
    friends_restaurant.close_restaurant()

    # Opens a restaurant called "Tin Tans" and tests all of the people served 
    # methods that were created.
    another_restaurant = Restaurant("Tin Tans", 
                                    "Soup",)
    print('')
    another_restaurant.open_restaurant()
    print(f'{another_restaurant.name} has served '
        f'{another_restaurant.number_served} customers so far.')
    another_restaurant.number_served = 10
    print(f'{another_restaurant.name} has served '
        f'{another_restaurant.number_served} customers so far.')
    another_restaurant.set_number_served(50)
    print(f'{another_restaurant.name} has served '
        f'{another_restaurant.number_served} customers so far.')
    another_restaurant.increment_number_served(3)
    print(f'{another_restaurant.name} has served '
        f'{another_restaurant.number_served} customers so far.')
    

def ice_cream_restaurant_methods():
    ice_cream_restaurant = IceCreamStandRestaurant("Dylan's Ice Shop", 
                                                   "Ice Cream",)
    # Print the "ice_cream_restaurant" name, and the flavors from .self 
    # directly.
    print(f'{ice_cream_restaurant.name} has these flavors today: '
          f'{ice_cream_restaurant.flavors}')
    # Call the method for getting the flavors using the ice cream shop that 
    # was made.
    ice_cream_restaurant.display_flavors()
    
restaurant_methods()
ice_cream_restaurant_methods()
