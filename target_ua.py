'''Lab 6.9'''
import random

def generate_grid():
    '''
    Generates a random grid
    '''
    grid = []
    alphabet_ua = ['а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', \
    'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с',\
    'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']
    while len(grid) < 5:
        litera = random.choice(alphabet_ua)
        
        if litera not in grid:
            grid.append(litera)
    return grid

def get_words(link, words):
    '''
    Checking words from dictinary
    >>> print("hello")
    hello
    '''
    good_words = []
    with open(link) as file:
        for word in file:
            word.strip()
            word.encode('utf-8')
            for i in range(len(word)):
                if word[i] == " ":
                    word, graphs = word[0:i], word[i:]
                    graphs = graphs.lstrip()
                    break
            if len(word) > 1 and len(word) <= 5:
                pass
            else:
                continue
            for i in words:
                if i == word[0]:
                    break
            else:
                continue

            if "noninfl" in graphs or "intj" in graphs:
                continue
            if graphs.startswith("/adv") or graphs.startswith("adv"):
                good_words.append((word, "adverb"))
                continue
            if graphs.startswith("/adj") or graphs.startswith("adj"):
                good_words.append((word, "adjective"))
                continue
            if "/n" in graphs or "noun" in graphs:
                good_words.append((word, "noun"))
                continue
            if "/v" in graphs:
                good_words.append((word, "verb"))
                continue
    return good_words

def check_user_words(entered_words, language, game_field, good_words):
    """
    Checks which of the user words meet the requirements and returns a list
    of words guessed
    >>> print("123")
    123
    """
    for i in range(len(entered_words) - 1):
        try:
            if len(entered_words[i]) > 5 or entered_words[i][0] not in game_field:
                del entered_words[i]
        except IndexError:
            break
    words_good = []
    not_entered_words = []
    for i in good_words:
        if i[0] not in entered_words:
            if i[1] == language: not_entered_words.append(i[0])
        elif i[0] in entered_words: 
            if i[1] == language: words_good.append(i[0])

    return words_good, not_entered_words

def get_user_words():
    """
    Input for user words
    """
    return input().lower().split()

def language_part_gen():
    """
    Random part of language
    """
    language = ['verb', 'noun','adverb', 'adjective']
    return random.choice(language)

def results():
    """
    Gets the results of the programm
    """
    game_field = generate_grid()
    language = language_part_gen()
    good_words = get_words("base.lst", game_field)
    user_words = get_user_words()
    correct_words, missed_words = check_user_words\
    (user_words, language, game_field, good_words)

print("hj")
