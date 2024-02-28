# Jake D'Esposito

def indexToCoords(i):
  return (i % 5, i // 5)

def coordsToIndex(x, y):
  return x + y * 5

for i in range(25):
  (x, y) = indexToCoords(i)
  assert coordsToIndex(x, y) == i, "Converting from index to coords and then back fails for index: " + str(i) + "!"

def playfairCipher(message, keyword=""):
    assert keyword.lower() == keyword, "Keyword needs to be all lower case letters!"
    assert message.lower() == message, "Message needs to be all lower case letters!"

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    assert set(keyword).issubset(set(alphabet)), "Keyword needs to consist of letters only!"
    assert set(message).issubset(set(alphabet)), "Message needs to consist of letters only!"

    combined = keyword + alphabet
    keys = sorted(set(combined), key=combined.index)
    keys.remove("j")

    del alphabet, combined

    key_table = []
    keys_copy = keys.copy()
    for _ in range(5):
        row = []
        for _ in range(5):
            row.append(keys_copy.pop(0))
        key_table.append(row)
    del keys_copy

    key_table_transpose = [[], [], [], [], []]
    for row in key_table:
        for i, x in enumerate(row):
            key_table_transpose[i].append(x)

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

    digrams = []
    for i in range(len(message) // 2):
        digrams.append((message[i * 2], message[i * 2 + 1]))

    encrypted_digrams = []
    for (a, b) in digrams:
        if a == "j":
            a = "i"
        if b == "j":
            b = "i"

        (ax, ay) = indexToCoords(keys.index(a))
        (bx, by) = indexToCoords(keys.index(b))

        if ay == by:
            new_a = key_table[ay][::-1][4 - ax - 1]
            new_b = key_table[by][::-1][4 - bx - 1]

            encrypted_digrams.append((new_a, new_b))
        elif ax == bx:
            new_a = key_table_transpose[ax][::-1][4 - ay - 1]
            new_b = key_table_transpose[bx][::-1][4 - by - 1]

            encrypted_digrams.append((new_a, new_b))
        else:
            new_a = key_table[ay][bx]
            new_b = key_table[by][ax]

            encrypted_digrams.append((new_a, new_b))

    return "".join([a + b for (a, b) in encrypted_digrams])

# Test cases from wiki.
for (question, answer) in [("hi", "bm"), ("de", "od"), ("th", "zb"), ("eg", "xd"), ("ol", "na"), ("di", "be"), ("nt", "ku"), ("he", "dm"), ("tr", "ui"), ("ex", "xm"), ("es", "mo"), ("tu", "uv"), ("mp", "if"), ("hidethegoldinthetreestump", "BMODZBXDNABEKUDMUIXMMOUVIF".lower())]:
    ans = playfairCipher(question, "playfairexample")
    assert ans == answer, f"The input {question} expected {answer}, but got {ans}!"

# Our test cases