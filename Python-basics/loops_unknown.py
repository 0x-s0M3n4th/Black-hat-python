# Write your code here :-)
name = '' # empty strings are evaluated as False , jab tak empty rahega tab tak naam mangta rhega
while not name:
    print("Enter your name: ")
    name = input('> ')
print("How many guests will you have? " )
num_of_guests = input('> ')
if num_of_guests:
    print(f'Be sure to have enough room {name} for everyone, because {num_of_guests} guests are coming. ')
print('Done')
