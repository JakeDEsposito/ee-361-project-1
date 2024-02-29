'''
	Author: Jake D'Esposito
	Date: 2/28/2024
	Last Modified: 2/29/2024

	"Keyword in Context"

	Statement of Purpose:
	    This program will take a message, a keyword, and a question if it should or should not encrypt the message.
	    The program will then encrypt or decrypt the message using the keyword and playfairs cipher.
	    The program will test itself using assertions.


	INPUT:
		1) A message consisting of lowercase characters from "a" to "z"
		2) A keyword that will be used to encrypt and decrypt.
		3) A question that asks if the program should encrypt or decrypt.

	OUTPUT:
		1) The output is the encrypted or decrypted message.
		    1.1) The output of encryption is always the same.
		    1.2) The output of decryption can change as a result of data loss from the playfair cipher

	ASSUMPTIONS:
		1) The message consisting of lowercase characters from "a" to "z"
		2) The keyword consisting of lowercase characters from "a" to "z"
'''

# Converts the index of a 1-dimensional array, of length 25, into the coordinates of a 2-dimensional, 5 by 5, array.
def indexToCoords(i):
  return (i % 5, i // 5)

# An implementation of the playfair cipher in python
# @param {string} message, the message that is to be crypted. Should be lowercase letters from "a" to "z"
# @param {string} keyword, the keyword that is used to crypt the message. Should be lowercase letters from "a" to "z"
# @param {boolean} shouldEncrypt, if the message should be encrypted or decrypted.
def playfairCipher(message, keyword="", shouldEncrypt=True):
    # Checks to make sure the message and keyword are lowercase characters.
    assert keyword.lower() == keyword, "Keyword needs to be all lower case letters!"
    assert message.lower() == message, "Message needs to be all lower case letters!"

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Checks to make sure the message and keywords only consist of characters from the alphabet.
    assert set(keyword).issubset(set(alphabet)), "Keyword needs to consist of letters only!"
    assert set(message).issubset(set(alphabet)), "Message needs to consist of letters only!"

    # Creates the key for the playfair cipher.
    combined = keyword + alphabet
    keys = sorted(set(combined), key=combined.index)
    keys.remove("j")

    del alphabet, combined

    # Creates a 5 by 5 table using the key.
    # if key = [1, 2, 3, 4, 5, ..., 20, 21, 22, 23, 24, 25]
    # key_table = [
    #   [1, 2, 3, 4, 5],
    #   ...
    #   [20, 21, 22, 23, 24, 25]
    # ]
    key_table = []
    keys_copy = keys.copy()
    for _ in range(5):
        row = []
        for _ in range(5):
            row.append(keys_copy.pop(0))
        key_table.append(row)
    del keys_copy

    # Creates the transposed table of the key_table.
    key_table_transpose = [[], [], [], [], []]
    for row in key_table:
        for i, x in enumerate(row):
            key_table_transpose[i].append(x)

    # If the message should be encrypted, any repeating letters should have an "x" put in between them.
    if shouldEncrypt:
        letter_pairs = []
        for i in range(len(message) - 1):
            letter_pairs.append((message[i], message[i + 1]))
        message = ""
        for (a, b) in letter_pairs:
            if a == b:
                message += a + "x"
            else:
                message += a
        message += letter_pairs[-1][1]
        del letter_pairs

        if len(message) % 2 == 1:
            message += "x"

    # Creates the digrams
    # message = "abcd"
    # digrams = [("a", "b"), ("c", "d")]
    digrams = []
    for i in range(len(message) // 2):
        digrams.append((message[i * 2], message[i * 2 + 1]))

    # Encrypt or decrypt the digrams.
    crypted_digrams = []
    for (a, b) in digrams:
        # Map "j" to "i".
        if a == "j":
            a = "i"
        if b == "j":
            b = "i"

        # Find the coordinates of a and b in the 2d array.
        (ax, ay) = indexToCoords(keys.index(a))
        (bx, by) = indexToCoords(keys.index(b))

        if ay == by: # a and b are in the same column.
            table = key_table[ay]
            if shouldEncrypt:
                table = table[::-1]

            new_a = table[(4 if shouldEncrypt else 0) - (ax if shouldEncrypt else -ax) - 1]
            new_b = table[(4 if shouldEncrypt else 0) - (bx if shouldEncrypt else -bx) - 1]

            crypted_digrams.append((new_a, new_b))
        elif ax == bx: # a and b are in the same row.
            table = key_table_transpose[ax]
            if shouldEncrypt:
                table = table[::-1]

            new_a = table[(4 if shouldEncrypt else 0) - (ay if shouldEncrypt else -ay) - 1]
            new_b = table[(4 if shouldEncrypt else 0) - (by if shouldEncrypt else -by) - 1]

            crypted_digrams.append((new_a, new_b))
        else: # a and b create a box.
            new_a = key_table[ay][bx]
            new_b = key_table[by][ax]

            crypted_digrams.append((new_a, new_b))

    # Combine the digrams into a message.
    m = "".join([a + b for (a, b) in crypted_digrams])
    if shouldEncrypt: # No extra steps for encryption. Return the new message.
        return m
    else:
        if len(m) <= 2:
            return m

        # Remove "x"'s put in during encryption step.
        m_culled = ""
        prev = m[0]
        for i in range(1, len(m) - 1):
            next = m[i + 1]
            current = m[i]

            if not (prev == next and current == "x"):
                m_culled += current

            prev = current

        return m[0] + m_culled + next


# Test cases from wiki.
for (question, answer) in [("hi", "bm"), ("de", "od"), ("th", "zb"), ("eg", "xd"), ("ol", "na"), ("di", "be"), ("nt", "ku"), ("he", "dm"), ("tr", "ui"), ("ex", "xm"), ("es", "mo"), ("tu", "uv"), ("mp", "if"), ("hidethegoldinthetreestump", "BMODZBXDNABEKUDMUIXMMOUVIF".lower())]:
    ans = playfairCipher(question, "playfairexample")
    assert ans == answer, f"The input {question} expected {answer}, but got {ans}!"
    ans_decrypted = playfairCipher(ans, "playfairexample", False)
    assert ans_decrypted == question, f"The decrypted answer for {question} expects {question}, but got {ans_decrypted} from decrypting {ans}!"

# Our test cases
# for (question, answer) in [("tree", "")]