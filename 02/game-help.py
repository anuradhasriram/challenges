#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from __future__ import division

import itertools
import random

from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7

def draw_letters():
    return ''.join(random.choice(POUCH) for _ in range(NUM_LETTERS))

def input_word(draw):
    word = raw_input("Enter a word :")
    _validation(word, draw)
    return word

def _validation(word, draw):
    for letter in word:
    if not letter.upper() in draw:
        print 'One or many of the letters in the word are not in draw'
        exit()
        
    if not word.lower() in DICTIONARY:
        print 'Given word is not in the dictionary'
        exit()

    return 

def calc_word_value(word):
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)

def get_possible_dict_words(draw):
    newlist = list()
    list1 = _get_permutations_draw(draw) 
    for l in list1:
        if l.lower() in DICTIONARY:
            newlist.append(l)
     
    return newlist

def _get_permutations_draw(draw):
    fulllist = list()
    for i in range(NUM_LETTERS):
       fulllist.extend(map("".join, itertools.permutations(draw, i)))

    return fulllist

def max_word_value(words):
    return max(words, key=calc_word_value)

def main():
    draw = draw_letters()
    print('Letters drawn: {}'.format(', '.join(draw)))

    word = input_word(draw)
    word_score = calc_word_value(word)
    print('Word chosen: {} (value: {})'.format(word, word_score))

    possible_words = get_possible_dict_words(draw)

    max_word = max_word_value(possible_words)
    max_word_score = calc_word_value(max_word)
    print('Optimal word possible: {} (value: {})'.format(
        max_word, max_word_score))

    game_score = (word_score / max_word_score) * 100
    print('You scored: {:.1f}'.format(game_score))


if __name__ == "__main__":
   main()
