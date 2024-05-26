# Dylan Nelson
# May 10, 2024
# arbitrary_keyword_arguments.py

# Double asterisks indicates that the item "user_info" will be a dictionary
def build_profile(first, last, **user_info):
    '''Build the profile of an individual that can handle an arbitrary amount
    of data'''
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# In this case the user will always provide the first and last name, the rest 
# of the information provided is optional
user_profile = build_profile('jerry', 
                             'seinfeld', 
                             city='new york', 
                             age=37, 
                             hair_color='brown',)
print(user_profile)
