def welcome():
    '''Greets the players and collects the names of Player 1 and Player 2.'''
    print ("Welcome to tic tac toe!")
    print ("please enter your names.")
    name1 = input("Player 1: ")
    name2 = input("Player 2: ")
    print ("Thank you!")
    return name1, name2



def main():
    '''This is where the main function goes.'''
    name1, name2 = welcome()


# Don't worry about this, all this does is makes sure when you
# run "python tic_tac_toe.py" in Terminal, it will do whatever
# we put in the function "main()" above.
if __name__=='__main__':
    main()
