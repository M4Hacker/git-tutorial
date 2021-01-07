#!  /usr/bin/python3

# The random package is needed to choose a random number

import random
import os 

# Define the game in a function

def guess_loop():

    os.system('clear')

    print("Hello user")
    name = input("What is your name : ")

    # This is the number the user will have to guess , chosen randomly
    # in between 1 and 100
    
    os.system('clear')

    answer = input("Alright "+name+", do you want to play a game ? (yes / no) ")

    if answer == "yes" or "y":
        os.system('clear')
        print("I have in mind a number between 1 and 100 , can you find it ? ")
        print("Find the right number : ")

    elif answer == "no" or "n":
        os.system('clear')
        print("Ok bye, you're missing something out !")
        return
        
    else: 
        print("yes or no only !")

    number_to_guess = random.randint (1 , 100)
    # Replay the question until the user finds the correct number
    while True :
        try :
            # Read the number the user inputs
            guess = int(input())
            # Compare it to the number to guess
            if guess > number_to_guess :
                print ("The number to guess is lower")
            elif guess < number_to_guess :
                print ("The number to guess is higher")
            else :
            # The user found the number to guess , let ’s exit
                os.system('clear')
                print ("YEAAAAAH congratulations "+name+" you find the good number, it was indeed", guess)
                return
        # A ValueError is raised by the int() function if the user inputs something else than a number
        except ValueError as err :
            print ("Invalid input , please enter an integer")

# Launch the game
guess_loop()