'''
	Author: Vincent Cifone
	Date: 2/28/2024
	Last Modified: 3/4/2024

	"Keyword in Context"

	Statement of Purpose:
	    This program will take in the name of a text file, the provided a looped prompt for a keyword.
	    The program will find all instances of the keyword within the text file
	    and print to the console the keyword with the 2 words preceding and postceding it (the context)

	INPUT:
		1) Name of the text file
		2) Keyword to search for on loop
		    2.1) Input of the letter 'Q' or 'q' will quit the program

	OUTPUT:
		1) All outputs will be a combination of the keyword surrounded by contextual words
		    1.1) By default the output will be two words followed by the keyword followed by two words
		    1.2) If the keyword is either of the first or last two words of the file it will be missing
		            one or both preceding or post-ceding words respectively

	PROCESSING:****
		1) All contents within the text file will be read in and parsed into an array
		    1.1) Punctuation marks will be removed during the parsing process
		2) The user-input keyword will be queried and when found will start the generation
		    of a dictionary with the keyword as the key and the context the value
            2.1) The context will be stored in the value portion of the keywords dictionary
            2.2) Context will be stored as an ARRAY of PAIRS of PAIRS: [((__,__),(__,__)),...]
                2.2.1) The pair of pairs will be formatted as: ((precon1, precon2),(postcon1,postcon2))
                2.2.2) Some instances of context words, for the first and last two words in the array
                        will be stored as empty strings
        3) The context will be print to the screen after the entire array has been queried for instances of
            the keyword
            3.1) Output will be formatted: precon1 precon2 keyword postcon1 postcon2

	ASSUMPTIONS:
		1) The first and second word in the text file, if queried, will be missing 2 or 1 word, respectively
		2) The second to and last word in the text file, if queried, will be missing 1 or 2 words respectively
		3) Punctuation within the file is non-essential to context, and thus will be ignored/removed


	Exception/Error Handling:
		1) N/A

'''
import string
# Methods:
#########################################
# file2array
'''
    Purpose: Takes in the valid name of a text file and reads the contents
            into a single array of strings

    Pre: Passed a valid file name to instantiate the input stream variable

    Post: Returns an array of strings with all unnecessary punctuation removed

'''
def file2array(fileName):
    arr = []
    # Open file
    with open(fileName, 'r') as textFile:
        # Read in file to single string removing endline characters
        temp = textFile.read().replace('\n','')

        # Remove punctuation (not decimal points if numeric values)
        temp = removePunct(temp)

        # Convert string into an array of strings
        arr = temp.split(" ")
    # Return prepared strings for queries
    return arr

#########################################
# removePunct
'''
    Purpose: Takes a string and removes all punctuation within the string. Takes into consideration 
        the decimal points of floating point values

    Pre: Passed a string

    Post: Returns a string will all punctuation removed

'''
def removePunct(inStr):
    outStr = ""
    decimal = False

    # Increment through entire string
    for i in range(len(inStr)):
        if inStr[i].isnumeric() and inStr[i+1] == '.':
            decimal = True

        if inStr[i] not in string.punctuation:
            outStr += inStr[i]
        elif decimal == True:
            outStr += inStr[i]
            decimal = False

    return outStr

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

    Pre: Passed an array of strings and a keyword as query to find within the array

    Post: Returns a dictionary with the context words of the keyword stored in an array of pairs of pairs as the
            value in a dictionary where the keyword is the key

'''


def array2dict(keyWord, arr):
    dict = {keyWord: []}
    # loop through length of array
    for i in range(len(arr)):
        # when you hit an instance of the keyword
        if arr[i] == keyWord:
            # Get preceding words as a pair
            if i == 0:
                pair1 = ("", "")                        # first word
            elif i == 1:
                pair1 = ("", arr[i - 1])                # 2nd word
            else:
                pair1 = (arr[i - 2], arr[i - 1])        # any word 3rd on

            # Get post-ceding words as a pair
            if i == len(arr) - 1:
                pair2 = ("", "")                        # last word
            elif i == len(arr) - 2:
                pair2 = (arr[i + 1], "")                # 2nd to last word
            else:
                pair2 = (arr[i + 1], arr[i + 2])        # any word 3rd to last and before

            # Add words pairs to dictionary
            dict[keyWord].append((pair1, pair2))

    return dict


#########################################
# printDict
'''
    Purpose: Prints the contents of a key in a dictionary to console
    
    Pre: Passed a dictionary as an argument and a keyWord for repeated queries

    Post: Prints the context of the passed keyWord to the console

'''
def printDict(dict, keyWord):
    pairs = dict.get(keyWord)
    for pair in pairs:
        print(pair[0][0], pair[0][1], keyWord, pair[1][0], pair[1][1])

#########################################

# Main Driver Method
#########################################
if __name__ == '__main__':
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
                # Read file into array
                fileArr = file2array(fileName)

                # Prompt user for keyword, loop exits on 'Q'
                while (True):
                    # Prompt for program functionality
                    print("\nPlease enter a keyword to get a list of its contexts from the file: (ex. 'the')")
                    print("Note: Input 'Q' to quit the program")
                    keyWord = input("Selection: ")
                    # Interpret user input
                    if keyWord.upper() != "Q":
                        printDict(array2dict(keyWord, fileArr),keyWord)
                        input("\nPress Enter to continue...")  # Pause before looping
                    else:
                        break
                break
            except:
                print("Invalid file name: ", fileName)
        else:
            input("\nExiting 'Keyword in context'...\nPress Enter to continue...")  # Pause before looping
            break