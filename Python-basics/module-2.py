# Write your code here :-)
import sys
while True:
    print("Type 'exit' to exit from the loop: ")
    response = input('> ')
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
