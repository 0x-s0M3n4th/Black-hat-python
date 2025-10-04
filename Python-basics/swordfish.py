# Write your code here :-)
while True:
    print("Who are you? ")
    name = input('>')
    if name != 'joe':
        continue
    while True:
        print("Hello, Joe. What is the password? (It is a fish.)")
        password = input('> ')
        if password != 'swordfish':
            continue
        else:
            break
    break
print("Access granted")
