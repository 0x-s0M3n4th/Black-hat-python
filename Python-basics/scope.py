# Write your code here :-)
def scope():
    rice = 'is there'
    print(rice)
scope()
#print(rice)

def spam():
    world = 'dinosaurs'
    bof()
    print(world)

def bof():
    hashtag = 'hashtag' # LOCAL VARIABLE
    vishnu = 'barahamihir'
    print(hashtag)
    print(vishnu)
spam()
print()


def testing():
    print(eggs)
eggs = 'SPAMSPAM' # GLOBAL VARIABLE
testing()
print(eggs)
print()

# Local variables and Global variables can have the same names.
def glo():
    spam = 'HELLO WORLD'
    print(spam)
def loc():
    spam = 'HELLO WORLD DUPLICATE'
    print(spam)
    glo()
    print(spam)

spam = 'GLOBAL'
loc()
print(spam)

# OUTPUT:
'''

HELLO WORLD DUPLICATE
HELLO WORLD
HELLO WORLD DUPLICATE
GLOBAL
'''

# Modifying a global variable:
earth = 'Earth is round' # Global variable

def modifying_global_var():
    global earth
    earth = 'Earth is not round!'# Modified the 'earth' value from 'Earth is round' to 'Earth is not round'
    print(earth)
modifying_global_var()
print(earth)


# Scope identification rules:
sister = 'is having all access' # Global variable
def brother():
    global sister
    sister = 'Modified the access by her brother!' # using the global variable

def mother():
    sister = 'Do the chores, ordered by mother, because no access infront of mother!' # Local variable

def father():
    print(sister) # Global variable , because the function only uses the variable, never assigned to this same variable

brother()
print(sister) # returned the answer from the `brother` function




