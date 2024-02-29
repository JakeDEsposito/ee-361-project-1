'''
    Authors:
        Jake D'Esposito
        Vincent Cifone
    Class: EE361: Fundamentals of Software Engineering
	Date: 2/27/2024
	Last Modified: 2/29/2024

	"EE361: Project 1"

	Statement of Purpose: This is the main driver file for running the solutions for the following problems
	    of EE361: Project 1

	    1. Liu Hui's PI algorithm
	    2. The Playfair cipher
	    3. Keyword in context

	INPUT:
		1)

	OUTPUT:
		1)

	PROCESSING:
		1)

	ASSUMPTIONS:
		1)

	Exception/Error Handling:
		1)

'''
# Libraries
from LiuHuiPI import *
from PlayfairCipher import *
from KeyWordContext import *

# 			Methods:
################################################
# Header Rubrick
'''
    Purpose: 

    Magnitude : O()

    Pre: ...

    Post: Returns...

'''

# Main Program

# Main menu loop
while (True):
    # Prompt for program functionality
    print("\nWhich part of the project would be executed? (input # from bellow)")
    print("1. Liu Hiu's PI algorithm")
    print("2. The Playfair cipher")
    print("3. Keyword in context")
    print("4. Exit")
    user_input = input("Selection: ")
    # Interpret user input
    if user_input == "1":
        #problemOne()
        print("Problem One...")
    elif user_input == "2":
        #problemTwo()
        print("Problem One...")
    elif user_input == "3":
        problemThree()
    else:
        break
    input("\nPress Enter to continue...")  # Pause before looping