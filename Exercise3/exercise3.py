def fun1(word):
    word = word.lower()
    return word[0:] == word[::-1]


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

    word_maximum_frequency = [word[0] for word in word_frequency.items() if word[1] == max(word_frequency.values())]

    return word_maximum_frequency


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


##need to be removed before submit
if __name__ == "__main__":
    print(fun1("radar"))
    print(fun1("a"))
    print(fun1("abc"))
    print(fun1("Dad"))
    print(fun1("red ER"))

    print(fun2("hjklTttTT233333@@@@@กกกกก"))
    print(fun2("@@@@@******"))

    print(fun3("gg  1234556   $$$"))
