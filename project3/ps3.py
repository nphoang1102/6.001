# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    # Clean word first and setup some storage here
    s = word.lower()
    comp1 = 0
    comp2 = 0

    # First score component based on scrabble letter values
    for char in s:
        comp1 += SCRABBLE_LETTER_VALUES.get(char, 0)

    # Calculating the length reward, beware the parentheses
    comp2 = max(1, (7 * len(s) - 3 * (n - len(s))))

    # Return word score and terminate
    return comp1 * comp2

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    # Add one wild card here
    hand['*'] = 1

    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    # Defining new hand to return and clean up input word just in case
    new_hand = dict(hand)
    s = word.lower()

    # Iterating through the word and removing characters from hand
    for char in s:
        new_hand[char] = new_hand.get(char, 0) - 1
        if (new_hand.get(char) < 1):
            del(new_hand[char])

    # Return the updated hand and terminate
    return new_hand

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    # Define temporay hand for mutating and clean up word
    s = word.lower()
    hand_check = dict(hand)

    # Check if the player constructs this 
    # based on whatever (s)he is having on hand
    for char in s:
        hand_check[char] = hand_check.get(char, 0) - 1
        if (hand_check.get(char) < 0):
            return False

    # Check if word is in fact in the word_list
    if ('*' not in s):
        if s in word_list:
            return True
    # Now check for the case of wild card, basically clone
    # the initial word and check vowel by vowel
    else:
        wild_card = s
        for v in VOWELS:
            replace = wild_card[0:wild_card.index('*')] + v + wild_card[wild_card.index('*') + 1:]
            if replace in word_list:
                return True

    # What are you doing here you invalid input?
    return False

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    # Setup variable for storing hand len
    len = 0

    # Iterating through hand and cound
    for key in hand:
        len += hand.get(key)

    # Return hand length and terminate
    return len

def play_hand(hand, word_list):
    # Storage variable
    score = 0

    # Start loop
    while calculate_handlen(hand) > 0:
        # Displaying information and prompt for input
        print()
        print('Current hand: ', end = '')
        display_hand(hand)
        word = input('Enter word, or "!!" to indicate that you are finished: ')
        
        # Check termination condition
        if (word == '!!'):
            break

        # Else update score
        else:
            # Validation
            if (is_valid_word(word, hand, word_list)):
                add = get_word_score(word, calculate_handlen(hand))
                score += add
                print('"' + word + '"', end = '')
                print(' earned', add, 'points. Total:', score, 'points')
            # Prompt invalid input:
            else:
                print('That is not a valid word. Please choose another word.')

        # Update hand anyway
        hand = update_hand(hand, word)
        if (calculate_handlen(hand) == 0): 
            print('Ran out of letters. ', end = '')

    # Display final score and terminate
    print('Total score:', score, 'points')
    return None

# Test case, chilling here
# hand = {'a':1, 'c':1, 'i':1, 'f': 1, '*':1, 't':1, 'x': 1}
# word_list = load_words()
# play_hand(hand, word_list)



#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    # If letter is not in hand, return hand
    if hand.get(letter, 0) == 0:
        return hand

    # Cloning hand just in case
    substituted_hand = dict(hand)

    # Substitute the letter into the player hand, re-roll of we get
    # the letter already in player's hand
    substitution = random.choice(string.ascii_lowercase)
    while hand.get(substitution, 0): 
        substitution = random.choice(string.ascii_lowercase)
    substituted_hand[substitution] = substituted_hand.pop(letter)

    # Return updated hand and terminate
    return substituted_hand

# Test cases just chilling here
# hand = {'h':1, 'e':1, 'l':2, 'o':1}
# print(substitute_hand(hand, 'h'))
# print(substitute_hand(hand, 'e'))
# print(substitute_hand(hand, 'l'))
# print(substitute_hand(hand, 'o'))
# print(substitute_hand(hand, 'a'))
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    print("play_game not implemented.") # TO DO... Remove this line when you implement this function
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
# if __name__ == '__main__':
#     word_list = load_words()
#     play_game(word_list)
