'''
	Author: Vincent Cifone
	Date: 2/28/2024
	Last Modified: 3/4/2024

	"Keyword in Context"

	Statement of Purpose:
	    This program will take in the name of a text file, the provide a looped prompt for a keyword.
	    The program will find all instances of the keyword within the text file
	    and print to the console the keyword with the 2 words preceding and postceding it (the context)

	INPUT:
		1) Name of the text file via command line argument
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
		1) Will produce an error message if the file fails to open due to invalid file name

'''
# Libraries:
#########################################
import string
import sys
# Methods:
#########################################
# file2array
def file2array(fileName):

    '''
        Purpose: Takes in the valid name of a text file and reads the contents
                into a single array of strings

        :param fileName: a valid file name to instantiate an input stream variable
        :returns: an array of strings
    '''
    arr = []
    # Open file
    with open(fileName, 'r') as textFile:
        # Read in file to single string removing endline characters
        temp = textFile.read().replace('\n',' ')

        # Remove punctuation (not decimal points if numeric values)
        temp = removePunct(temp)

        # Remove instances of multiple spaces
        temp = ' '.join(temp.split())

    # Convert string into an array of strings and return
    return temp.split(' ')

#########################################
# removePunct
def removePunct(inStr):
    '''
        Purpose: Takes a string and removes all punctuation within the string. Takes into consideration
            the decimal points of floating point values

        :param inStr: a string of characters
        :returns: a string will all punctuation removed
    '''
    outStr = ""
    decTim = False      # boolean to indicate a decimal or time format of a string was discovered

    # Increment through entire string
    for i in range(len(inStr)):
        if inStr[i].isnumeric() and (inStr[i+1] == '.' or inStr[i+1] == ':'):
            decTim = True

        # Inspect if the current character is considered punctuation
        if inStr[i] not in string.punctuation:
            outStr += inStr[i]
        elif decTim == True:
            outStr += inStr[i]
            decTim = False

    return outStr

#########################################
# array2dict
def key2pairs(keyWord, arr):
    '''
        Purpose: Takes an array of strings and a keyword and find each instance of the
            keyword within the array and its context words
            Each of the keywords *2 words preceding and post-ceding context words
            will be returned as an array of pairs of pairs

        ** There is an assumption that if an instance of the keyword is not pre- or post-ceded by
        2 words, the context can still be stored for 1 or 0 words

        Array Format:
        [(("",""),("","")),...]
        :param keyWord: a keyword as search query
        :param arr: an array of strings
        :returns: Returns an array of pairs of pairs representing the context words of the keyword within the array
    '''
    pairArr = []
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
            pairArr.append((pair1, pair2))

    return pairArr


#########################################
# printDict
def printDict(dict, keyWord):
    '''
        Purpose: Prints the contents of a key in a dictionary to console
        :param dict: a dictionary as an argument
        :param keyWord: a keyWord for repeated queries
        :returns: Prints the context of the passed keyWord to the console
    '''
    pairs = dict.get(keyWord)
    for pair in pairs:
        print(pair[0][0], pair[0][1], keyWord, pair[1][0], pair[1][1])


#########################################

# Main Driver
#########################################
if __name__ == '__main__':

    # Access file name from command line arg
    print('args',sys.argv)
    fileName = sys.argv[1]

    # Dictionary to hold keywords and their respective contexts
    dic = {}

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
                # If not current instance of keyword in dictionary
                if(keyWord not in dic):
                    dic[keyWord] = key2pairs(keyWord,fileArr)
                    printDict(dic,keyWord)
                else:
                    printDict(dic,keyWord)

                input("\nPress Enter to continue...")  # Pause before looping
            else:
                input("\nExiting 'Keyword in context'...\nPress Enter to continue...")  # Pause before looping
                break
    except:
        print("Invalid file name: ", fileName)
