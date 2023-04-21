import random
def game(choice):
    computer_choice = random.choice('knbsl')
    if computer_choice == choice:
        print(computer_choice)
        return 'tie'
    elif computer_choice == 'k' and choice == 'n':
        print(computer_choice)
        return 'AI win'
    elif computer_choice == 'k' and choice == 'b':
        print(computer_choice)
        return 'you win'
    elif computer_choice == 'n' and choice == 'k':
        print(computer_choice)
        return 'you win'
    elif computer_choice == 'n' and choice == 'b':
        print(computer_choice)
        return 'AI win'
    elif computer_choice == 'b' and choice == 'n':
        print(computer_choice)
        return  'you win'
    elif computer_choice == 'b' and choice == "k":
        print(computer_choice)
        return  'AI win'
    elif computer_choice == 'l' and choice == "b":
        print(computer_choice)
        return  'AI win'
    elif computer_choice == 'l' and choice == "s":
        print(computer_choice)
        return  'AI win'
    elif computer_choice == 'b' and choice == 'l':
        print(computer_choice)
        return  'you win'
    elif computer_choice == 's' and choice == 'l':
        print(computer_choice)
        return  'you win'
    elif computer_choice == 'l' and choice == 'k':
        print(computer_choice)
        return  'you win'
    elif computer_choice == 'k' and choice == 'l':
        print(computer_choice)
        return  'AI win'
    elif computer_choice == 'b' and choice == "s":
        print(computer_choice)
        return  'AI win'
    elif computer_choice == 's' and choice == "k":
        print(computer_choice)
        return  'AI win'
    elif computer_choice == 'k' and choice == 's':
        print(computer_choice)
        return  'you win'
    elif computer_choice == 'n' and choice == 's':
        print(computer_choice)
        return  'you win'
    elif computer_choice == 's' and choice == "n":
        print(computer_choice)
        return  'AI win'
    elif computer_choice == 'n' and choice == "l":
        print(computer_choice)
        return  'AI win'