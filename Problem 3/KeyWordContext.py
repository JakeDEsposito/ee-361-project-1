'''
	Author: Vincent Cifone
	Date: 2/28/2024
	Last Modified: 3/8/2024

	"Keyword in Context"

	Statement of Purpose:
	    This program will take in the name of a text file, the provide a looped prompt for a keyword.
	    The program will find all instances of the keyword within the text file
	    and print to the console the keyword with the 2 words preceding and post-ceding it (the context)

	INPUT:
		1) Name of the text file via command line argument
		2) Keyword to search for on loop
		    2.1) Input of the letter 'Q' or 'q' will quit the program

	OUTPUT:
		1) All outputs will be a combination of the keyword surrounded by contextual words
		    1.1) By default the output will be two words followed by the keyword followed by two words
		    1.2) If the keyword is either of the first or last two words of the file it will be missing
		            one or both preceding or post-ceding words respectively

	PROCESSING:
		1) All contents within the text file will be read in and parsed into an array
		    1.1) Punctuation marks will be removed during the parsing process
		2) The user-input keyword will be queried by loop and when found will start the generation
		    of an array the contexts of the keyword
            2.1) Context will be stored as an ARRAY of PAIRS of PAIRS: [((__,__),(__,__)),...]
                2.2.1) The pair of pairs will be formatted as: ((precon1, precon2),(postcon1,postcon2))
                2.2.2) Some instances of context words, for the first and last two words in the array
                        will be stored as empty strings
            2.2) After the context has been parsed from the original array of strings, the context array for
                    the keyword will be added as the value of the keyword in a dictionary
        3) The context of the keyword will be print to the screen from the data stored within the dictionary
            3.1) Output will be formatted: precon1 precon2 keyword postcon1 postcon2

	ASSUMPTIONS:
		1) The first and second word in the text file, if queried, will be missing 2 or 1 word, respectively
		2) The second to and last word in the text file, if queried, will be missing 1 or 2 words respectively
		3) Punctuation within the file is non-essential to context, and thus will be ignored/removed
		4) Keyword matching will be case sensitive
		5) Input file will only contain ASCII characters

	Exception/Error Handling:
		1) Will produce an error message if the file fails to open due to invalid file name


    Design Decisions:
        1) The choice to read the file initially into a string was made to allow for the use string manipulation
            to remove endline characters, unnecessary punctuation and duplicate spaces with ease before converting
            the string into an array of strings for queries
        2) The choice to have the files contents recorded as an array of strings for queries was to utilize the array
            indexing to check for pre and post contextual words to capture when creating the array of pairs of pairs
            to represent the keywords context
        3) The choice to use an array of pairs of pairs to hold the contextual words for a given keyword was to allow
            for all the contextual words of a keyword to be stored within they value of the keywords key in a dictionary
            3.1) The choice to use a pair of pairs for each context was to allow the seperation and ease of indexing for
                    the pre-contextual words and the post-contextual words during output
        4) The format of the dictionary was chosen to utilize the keyword as the key with the attributed value as
            an array of pairs (of context) to allow for indexing ease for each value (pair of pairs) for the keyword

    Test Case Decisions:
        1) Test File #1: test1.txt
            1.1) File contains instances of punctuation to interpret
            1.2) File contains instances of multiple spaces between words

            1.3) Keyword Query #1: 'no'
                1.3.1) Tests for keyword close to the end of the file
                    1.3.1.1) should have an output with only ONE contextual post-word
                1.3.2) keyword in initial file would be followed by punctuation
                    1.3.2.1) instance of punctuation is not recorded and thus allows for proper query of word
                1.3.3) Results:
                    "443.289 wait no more"
                1.3.4) Discussion:
                    1.3.4.1) The processing successfully removes instances of punctuation
                    1.3.4.2) The processing successfully displays only one post-context word for the keyword
            1.4) Keyword Query #2: '443.289'
                1.4.1) Tests for keyword where punctuation should not be removed due to formatting of element
                    1.4.1.1) keyword is a numeric decimal and thus needs the decimal point to maintain purpose
                1.4.2) keyword in initial file would be followed by punctuation
                    1.4.2.1) multiple instances of punctuation involved in processing of keyword
                1.4.3) Results:
                    "only THREE 443.289 wait no"
                1.4.4) Discussion:
                    1.3.4.1) The processing successfully removes instances of punctuation
                    1.3.4.2) The processing successfully displays both context words for the keyword
                    1.3.4.3) The processing successfully displays the required decimal point for the keyword

        2) Test File #2: test2.txt
            2.1) Keyword Query #1: 'Is'
                2.1.1) Tests for keywords at the very beginning of the file.
                    2.1.1.1) The first output should have 'Is' followed by two words.
                2.1.2) Punctuation should be removed.
                2.1.3) Results:
                    "Is this the"
                    "real life Is this just"
                2.1.4) Discussion:
                    2.1.4.1) The processing successfully processed input at beginning of the file.
                    2.1.4.2) The processing successfully removes instances of punctuation.

            2.2) Keyword Query #2: 'this'
                2.2.1) Test for keywords that is near the beginning of the file.
                    2.2.1.1) The first output should have one word before the chosen word.
                2.2.2) Results:
                    "Is this the real"
                    "life Is this just fantasy"
                    "back again this time tomorrow"
                    "life from this monstrosity Easy"
                    "cant do this to me"
                2.2.3) Discussion:
                    2.2.3.1) The processing successfully processed the input at the second position of the file.

            2.3) Keyword Query #3: 'to'
                2.3.1) Test for keywords that is near the end of the file.
                    2.3.1.1) The last output should have one word after the chosen word.
                2.3.2) Results:
                    "look up to the skies"
                    "really matter to me to"
                    "to me to me Mama"
                    "didnt mean to make you"
                    "Ive got to go Gotta"
                    "leave me to die Oh"
                    "do this to me baby"
                    "really matters to me"
                2.3.3) Discussion:
                    2.3.3.1) The processing successfully processed the input at the second to last position of the file.

        3) Test File #3: test3.txt
            3.1) File contains instances of punctuation to interpret
            3.2) File contains instances of multiple ambiguous punctuation between words
            3.3) File contains multiple lines of input to process
            3.4) File contains multiple instances of the same word
            3.5) File contains multiple instances of the same word with different cases

            3.6) Keyword Query #1: 'two'
                3.6.1) Tests a keyword with known multiple instances within the input file
                3.6.3) Results:
                    "were only two words now
                    one or two lines for
                    ask if two cases should"
                3.6.4) Discussion:
                    3.6.4.1) The processing successfully removes instances of punctuation
                    3.6.4.2) The processing successfully displays each instance of both context words for the keyword
                    3.6.4.3) The processing successfully only captures matched cases of the keyword
            3.7) Keyword Query #2: 'Two'
                3.7.1) Tests a keyword with multiple instances within the same file, but with a different case
                3.7.2) Results:
                    "of only Two words there"
                3.7.3) Discussion:
                    3.7.3.1) The processing successfully removes instances of punctuation
                    3.7.3.2) The processing successfully displays each instance of both context words for the keyword




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
