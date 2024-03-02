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
import string
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
    arr = []
    # Open file
    with open(fileName, 'r') as textFile:
        # Read in file to single string removing endline characters
        temp = textFile.read().replace('\n','')

        # Remove punctuation (not decimal points if numeric values)
        temp = removePunct(temp)

        # Convert string into an array of strings
        arr = temp.split(" ")

    return arr

#########################################
# removePunct
'''
    Purpose: Takes a string and removes all punctuation within the string. Takes into consideration 
        the decimal points of floating point values

    Magnitude : O()

    Pre: ...

    Post: Returns...

'''
def removePunct(inStr):
    outStr = ""
    decimal = False

    for char in inStr:
        if char in string.punctuation:
            if char == '.' and not decimal:
                outStr += char
                decimal = True
        else:
            outStr += char
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

    Magnitude : O()

    Pre: ...

    Post: Returns...

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
    Magnitude : O()

    Pre: ...

    Post: Returns...

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