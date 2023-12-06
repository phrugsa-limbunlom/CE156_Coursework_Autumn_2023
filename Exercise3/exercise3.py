# the function receive a word (string) as an input argument
# convert the input word to be all lowercase to avoid sensitive case
# then using a slide window to verify whether the original word from front to back
# and the reverse from back to front is all the same for every character or not
# then return the verification as a boolean (True of False) to whether if the given word is palindrome
def fun1(word):
    word = word.lower()
    return word[0:] == word[::-1]


# the function receive a word (string) as an input argument
# convert the input word to be all lowercase to avoid sensitive case
# for loop all characters in the word and verify if each character is digit or letter
# then retain that character with its frequency occurrence in the dictionary if it is digit or letter
# also checking whether there are no letters or digits by counting a number of character if it is not digit or letter
# if count number is 0, then the function returns None
# if not, for loop all words (key) in the dictionary to find the maximum occurrences (value) of that/those character/characters
# then return the frequency for a character having the most occurrence
def fun2(word):
    word = word.lower()
    word_frequency = dict()
    count = 0
    for w in word:
        if w.isdigit() or w.isalpha():
            if w not in word_frequency:
                word_frequency[w] = 1
            else:
                word_frequency[w] = word_frequency[w] + 1
            count += 1
    if count == 0:
        return None

    character_maximum_frequency = [word[0] for word in word_frequency.items() if word[1] == max(word_frequency.values())]

    return character_maximum_frequency[len(character_maximum_frequency)-1]


# the function receive a word (string) as an input argument
# inside the function, initialize a dictionary with three groups (letter, space, digit) as three keys with 0 value
# for loop all characters in the word and check if it is a letter, a space, or a digit
# if it is a letter, assign it as a letter group in a dictionary by count a number of frequency (value) of letter (key)
# if it is a space, assign it as a space group in a dictionary by count a number of frequency (value) of space (key)
# if it is a digit, assign it as a digit group in a dictionary by count a number of frequency (value) of digit (key)
# if it is not in any above group, it will not be assigned to any group
# then convert the dictionary to a tuple and return the tuple as an output
def fun3(word):
    word_count_dict = {"letter": 0, "space": 0, "digit": 0}
    for w in word:
        if w.isalpha():
            word_count_dict["letter"] = word_count_dict["letter"] + 1
        elif w.isspace():
            word_count_dict["space"] = word_count_dict["space"] + 1
        elif w.isdigit():
            word_count_dict["digit"] = word_count_dict["digit"] + 1
        else:
            continue

    word_count_tuple = [(k, v) for k, v in word_count_dict.items()]
    return word_count_tuple
