VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    """In the while loop ask the user to enter a color,
       lowercase it and store it in a variable. Next check: 
       - if 'quit' was entered for color, print 'bye' and break. 
       - if the color is not in VALID_COLORS, print 'Not a valid color' and continue.
       - otherwise print the color in lower case."""
    while True:
        choice = input("Enter a color: ")
        if choice == 'quit':
            print('bye')
            break
        elif choice in VALID_COLORS:
            print(choice.lower())
        else:
            print('Not a valid color')
            

print_colors()
