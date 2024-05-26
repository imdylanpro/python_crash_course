# Dylan Nelson
# May 13, 2024
# users.py

class User:
    '''Creates an instance of a user. Requires a first and last name.'''

    def __init__(self, first_name, last_name):
        '''Assigns the first name and last name to the user'''
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = (f'{first_name} {last_name}') 
        self.login_attempts = 0

    def describe_user(self):
        '''Describes the user using their first and last name.'''
        print(f"User's name is {self.first_name} {self.last_name}.")

    def greet_user(self):
        '''Greets the user'''
        print(f"Hello {self.first_name}.")

    def increment_login_attempts(self, attempts = 1):
        '''Increments the amount of attempts a user has made to log in.\n
        Default value is 1, can set a custom number of attempts.'''
        print(f'{self.full_name} failed login attempt. ' 
              f'Incrementing failed login attempts by {attempts}. ')
        self.login_attempts += attempts
        print(f'New number of log in attempts for {self.full_name} '
              f'is {self.login_attempts}.')

    def reset_login_attempts(self):
        '''Resets the number of log in attempts that a user's account has.'''
        print(f"Resetting {self.full_name}'s log in attempts to 0.")
        self.login_attempts = 0

class Admin(User):
    '''Creates an instance of an admin, which is a special kind of user 
    profile, meaning that this class will inherit from the "User" class.'''

    def __init__(self, first_name, last_name):
        '''Initialize the admin user, requiring a first and last name.'''
        self.privileges = Privileges()
        super().__init__(first_name, last_name)
        '''Utilize the first_name, last_name from the User class.'''

class Privileges():
    '''Creates an instance of a privilege. \n
    Attributes: "privileges".\n
    Methods: "show_privileges", "set_privileges".'''
    def __init__(self):
        self.privileges = []

    def set_privileges(self, input):
        '''Allows for privileges to be added to an "Admin" priviledges list.'''
        print(f'Adding privilege: "{input}".')
        self.privileges.append(input)

    def show_privileges(self):
        '''Prints the privileges associated with the Admin.'''
        print(f"The user's privileges are: {self.privileges}.")

# Print out all of the users
def user_methods_function(incrementer):
    '''Executes the methods that were created for the "User" class. '''

    for u in users:
        u.describe_user()
        u.greet_user()
        u.login_attempts = incrementer
        incrementer += 2
        print(f"User {u.full_name} has "
        f"{u.login_attempts} attempted logins.")
        u.increment_login_attempts(starter_attempts)
        u.reset_login_attempts()

def admin_methods_function():
    '''Executes the methods that were created for the "Admin" class.'''

    admin1.privileges.show_privileges()
    admin1.privileges.set_privileges('can ban users')
    admin1.privileges.show_privileges()

# Create three instances of the users using the "User" class
user1 = User('Dylan', 'Nelson')
user2 = User('Mark', 'Plumber')
user3 = User('Jacob', 'Ham')
users = [user1, user2, user3]
starter_attempts = 1

admin1 = Admin('Julia', 'Peterson')

# user_methods_function(starter_attempts)
admin_methods_function()
    
