# Dylan Nelson
# May 10, 2024
# user_profile.py

# Build a personal profile that includes first and last name as a requirement,
# and anything else that the user wants to include

def user_profile(first, last, **user_info):
    '''Creates a dictionary with the supplied information'''
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# The key value pairs are established here:
# ('age': '25') and ('height': '6 feet')
profile = user_profile('dylan', 
             'nelson', 
             age=25, 
             height='6 feet',
             shoe_size=10.5)

print(profile)
