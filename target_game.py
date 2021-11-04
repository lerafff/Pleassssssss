'''Lad 6.5'''
from typing import List
import random
import string

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    abc = []
    letters =[]
    for i in range (65, 91):
        abc.append(chr(i))
    for b in range(3):
        letters.append(random.sample(abc,3))
    return letters


def get_words(file: str, string_1: List[str]) -> List[str]:
    """
    Reads the file
    >>> get_words('en.txt', [el for el in 'wumrovkif'])
    ['fork', 'form', 'forum', 'four', 'fowk', 'from', 'frow', 'irok', 'komi', \
'kori', 'miro', 'miro', 'moki', 'ovum', 'work', 'worm', 'wouf']
    """
    alpab = list(string.ascii_lowercase)
    alp = []
    for i in alpab:
        if i in string_1:
            continue
        else:
            alp.append(i)

    with open(file) as file:
        result_1 = []
        file.readline()
        file.readline()
        for line in file:
            line = line.lower() 
            line = line[:-1]
            not_add = False
            if len(line) >= 4 and string_1[4] in line:
                for i in alp:
                    if i in line:
                        not_add = True
                        break
                    for j in string_1:
                        if line.count(j) > string_1.count(j):
                            not_add = True
                            break
                if not_add:
                    not_add = False
                    continue
                else:
                    result_1.append(line)
    return result_1
 
def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    return input().lower().split()
        
def get_pure_user_words(words_user: List[str], string_1: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    for i in words_from_dict:
        if i in words_user:
            words_user.remove(i)

    alpab = list(string.ascii_lowercase)
    alp = []
    for i in alpab:
        if i in string_1:
            continue
        else:
            alp.append(i)
    result_1 = []
    for word in words_user:
        not_add = False
        if len(word) >= 4 and string_1[4] in word:
            for i in alp:
                if i in word:
                    not_add = True
                    break
                for j in string_1:
                    if word.count(j) > string_1.count(j):
                        not_add = True
                        break
            if not_add:
                not_add = False
                continue
            else:
                result_1.append(word)

    return result_1

def results():
    '''
    Starting the game

    '''
    text = ''
    string_1 = generate_grid()
    print(string_1)
    for i in range(3):
        for j in range(3):
            text += string_1[i][j].lower()
    entered_words = get_user_words()
    right_words = get_words("en.txt", text)
    print(right_words)
    print(entered_words)
    logzni_words = get_pure_user_words(entered_words, text, right_words)
    entered_not = right_words
    print(entered_not)

    for i in entered_words:
        if i in right_words:
            entered_not.remove(i)
    correct_user_words = len(right_words) - len(entered_not)

    with open("result.txt", "w") as result:
        result.write(str(correct_user_words))
        result.write("\n")
        result.write(str(entered_not))
        result.write("\n")
        result.write(str(entered_words))
        result.write("\n")
        result.write(str(logzni_words))
        result.write("\n")
        result.close()

print("lll")
print("PPPP")
