from data import DICTIONARY, LETTER_SCORES

def load_words():
    with open(DICTIONARY) as dict:
        return[x.strip() for x in dict.readlines()]

def calc_word_value(word):
    return sum(LETTER_SCORES.get(letter.upper(), 0) for letter in word)

def max_word_value(listOfWords=None):
    #https://dbader.org/blog/python-min-max-and-nested-lists
    return max(listOfWords or load_words(), key= lambda x: calc_word_value(x))    


inputList = raw_input("Enter the input list with spaces : ").split()
if not inputList:
    wordWithMaxValue = max_word_value()
else:
    wordWithMaxValue = max_word_value(inputList)

print 'Max word is ' + wordWithMaxValue
