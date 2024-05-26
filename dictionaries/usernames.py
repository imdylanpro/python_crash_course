# Dylan Nelson
# February 13, 2024
# usernames.py

# This program will show an example of looping through a dictionary

# Creates a dictionary that utilizes vertical listing for ease of readability
user_0 = {
    'username': 'dylajelly',
    'first': 'Dylan',
    'last': 'Jordan',
}

# prints each key and value in the dictionary associated with user_0
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
