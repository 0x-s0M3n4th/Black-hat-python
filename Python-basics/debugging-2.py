sister = 'is having all access' # Global variable
def brother():
    global sister
    sister = 'Modified the access by her brother!' # using the global variable

def mother():
    sister = 'Do the chores, ordered by mother, because no access infront of mother!' # Local variable
    
def father():
    print(sister) # Global variable , because the function only uses the variable, never assigned to this same variable

brother()
print(sister)