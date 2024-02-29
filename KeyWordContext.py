'''
	Author: Vincent Cifone
	Date: 2/28/2024
	Last Modified: 2/29/2024

	"Keyword in Context"

	Statement of Purpose:
	    This program will take in the name of a text file and a keyword.
	    The program will then find all instances of the keyword within the text file
	    and print to the console the keyword with the 2 words preceding and postceding it


	INPUT:
		1) Name of the text file
		2) Keyword to search for

	OUTPUT:
		1) All outputs will be a combination of the keyword surrounded by contextual words
		    1.1) By default the output will be two words followed by the keyword followed by two words
		    1.2) If the keyword is either of the first or last two words of the file it will be missing
		            one or both preceding or post-ceding words respectively

	PROCESSING:****
		1) All contents within the text file will be read in and parsed into an array
		2) The keyword will be queried and when found captured as a substring with the
		    2* words preceding and post-ceding, which will be added to an array of strings
        3) The array of strings will be print to the console

	ASSUMPTIONS:
		1) The first and second word in the text file, if queried, will be missing 2 or 1 word, respectively
		2) The second to and last word in the text file, if queried, will be missing 1 or 2 words respectively


	Exception/Error Handling:
		1) N/A

'''
# Methods:
#########################################
# file2array
'''
    Purpose: Takes in the valid name of a text file and reads the contents
            into a single array of strings

    Magnitude : O()

    Pre: ...

    Post: Returns...

'''


def file2array(fileName):
    # while !fin
    # fin >> str
    # dynamArr[i] = str

    return


#########################################
# array2dict
'''
    Purpose: Takes an array of strings and a keyword and find each instance of the
        keyword within the array and its context words
        The keyword will be the basis for a dictionary, and each *2 words preceding and 
        post-ceding will be added to the keywords dictionary (pre-words and post-words)

    * There is an assumption that if an instance of the keyword is not pre- or post-ceded by 
    2 words, the context can still be stored for 1 or 0 words


    Dictionary Format:
    {keyword:[(("",""),("","")),...]}

    Magnitude : O()

    Pre: ...

    Post: Returns...

'''


def array2dict(keyWord, arr):
    # loop through length of array
    # when you hit an instance of the keyword
    # 1) capture the array elements from (inst -2, inst -1) and (inst +1,inst+2)
    # 2) append to dict.get(k) <-- array of pairs of pairs
    # Continue loop to next word

    return


#########################################
# printDict
'''
    Purpose: Prints the contents of a dictionary to console
    Magnitude : O()

    Pre: ...

    Post: Returns...

'''


def printDict(dict):
    # loop through length of value (of the keywords dict) (array of pairs of pairs)
    # for each value:
    # print pair1[1] pair1[2] key pair2[1] pair2[1] endl

    return

#########################################

# Main Driver Method
#########################################
# runKeyWordContext
'''
    Purpose: Prints the contents of a dictionary to console
    Magnitude : O()

    Pre: ...

    Post: Returns...

'''
def runKeyWordContext():
    # Prompt user for file name, loop test for valid file name
        while (True):
            # Prompt for program functionality
            print("\nPlease enter the file name for processing: ('____.txt')")
            print("Options:")
            print("1. pg10.txt")
            print("2. test1.txt")
            print("3. test2.txt")
            print("4. Exit")
            fileName = input("Selection: ")
            # Interpret user input
            if fileName != "4":
                try:
                    fin = open(fileName, "r")
                except:
                    print("Invalid file name: ", fileName)
                finally:
                    input("\nPress Enter to continue...")  # Pause before looping
                    continue
            else:
                input("\nPress Enter to continue...")  # Pause before looping
                break

    # Open file

    # Read file into array

    # Prompt user for keyWord, if Q exit,

    # Make dict from keyword

    # if keyword does not exist (value array is empty) print keyword not found)
    # else print contents of dictionary




