# Dylan Nelson
# June 18, 2024
# ordinal_numbers.py

ordinal_num = [1,2,3,4,5,6,7,8,9]
 
for num in ordinal_num:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num ==3:
        print(f"{num}rd")
    else:
        print(f"{num}th")