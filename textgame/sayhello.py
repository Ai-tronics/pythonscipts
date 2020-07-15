def say_hello():
    print('Hello, World!')

say_hello()

answer = input("Would you like another greeting? \n")

if answer == 'y':
    say_hello()
else:
    print("Fine...Be that way.")