def pretty_print_unordered(vals):
    for item in vals:
        print("* "+ str(item)) #create a new string object from the param

def pretty_print_ordered(vals):
    i = 1
    for item in vals:
        print(str(i) + " . " + str(item))
        i = i + 1

def pretty_print_ordered_range(vals):
    for i in range(len(vals)):
        print(str(i + 1) + " . " + str(vals[i]))

def pretty_print_ordered_tuple(vals):
    for i, data in enumerate(vals,1):
        print(str(i) + " . " + str(data))
        
        
favorites = []
more_items = True
while more_items:
    user_input = input("Enter something you like: \n")
    if user_input == '':
        more_items = False
    else:
        favorites.append(user_input)

print("Here are all the things you like!")
pretty_print_ordered_tuple(favorites)