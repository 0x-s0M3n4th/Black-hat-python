# Write your code here :-)
import random
secret_number = random.randint(1,20)
print("I have taken my guess between 1-20!")

for guess_taken in range(1,7):
    print('Take a guess kiddo.')
    guess = int(input('> '))

    if guess < secret_number:
        print("Your guess is too low!!")
    if guess > secret_number:
        print("Your gues is too high!!")
    else:
        break
if guess == secret_number:
    print('Good job! You got it in ' + str(guess_taken) + 'guesses. ')
else:
    print('Nope the number was ' + str(secret_number))

