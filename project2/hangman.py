# Problem Set 2, hangman.py
# Name: Hoang N
# Time spent: 115 mins

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

# Importing the words from the text file and return them
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

# Choose a random word from an available wordlist
def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

# Some debug parameters
# secret_word = 'apple'
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']

# Check if the word has been guessed or not
def is_word_guessed(secret_word, letters_guessed):
    # Iterating through the secret word and check if contained in geussed word
    for char in secret_word:
        if char in letters_guessed:
            continue
        else:
            return False
    
    # Only return true if secret words are all contained in letters guessed
    return True

# Test case for is_word_guessed funtion, gonna leave it chilling here 
# print(is_word_guessed(secret_word, letters_guessed))

# Get the guessed words up to this point
def get_guessed_word(secret_word, letters_guessed):
    # Storing variable for return here
    guessed_word = ''

    # If character has been guessed, display it, else display an underscore
    for char in secret_word:
        if char in letters_guessed:
            guessed_word += (char + ' ')
        else:
            guessed_word += '_ '

    # Return guessed word up to this point
    return guessed_word

# Test case for get_guessed_word function, gonna leave it chilling here
# print(get_guessed_word(secret_word, letters_guessed))

# Get whatever letters left that are still available for guessing
def get_available_letters(letters_guessed):
    # Storing variable for return here
    available_letters = ''

    # If character has been guessed, ignore it, else add it to the available letter
    for char in string.ascii_lowercase:
        if char in letters_guessed:
            continue
        else:
            available_letters += char

    # Return list of available letter here
    return available_letters

# Test case fir get_available_letters function, gonna leave it chilling here
# print(get_available_letters(letters_guessed))

def hangman(secret_word):
    # Setup some variables to store the game parameters
    warnings = 3
    guesses = 6
    letters_guessed = ''
    vowels = 'aeiou'

    # Welcome text
    print('Welcome to the game Hangman')
    print('I am thinking of a word that is', len(secret_word), 'letters long:', get_guessed_word(secret_word, letters_guessed))

    # Game start
    while not is_word_guessed(secret_word, letters_guessed):
        # End game if the player ran out of guesses
        print('----------------')
        if (guesses == 0):
            print('Sorry, you ran out of guesses. The word was:', secret_word)
            return None

        # Information prompting
        available_letters = get_available_letters(letters_guessed)
        print('You have', guesses, 'guesses left.')
        print('Available letters:', available_letters)
        guessed_char = str.lower(input('Please guess a letter: '))
        
        # Check for valid input first
        if (len(guessed_char) != 1) or (guessed_char not in string.ascii_lowercase):
            if warnings:
                warnings -= 1
            else:
                guesses -= 1
            print('Oops! That is not a valid letter. You have', warnings, 'warnings left:', get_guessed_word(secret_word, letters_guessed))
        
        # Check for input char next
        else:
            # Check for already guessed letter
            if guessed_char in letters_guessed:
                if warnings:
                    warnings -= 1
                else:
                    guesses -= 1
                print("Oops! You've already guessed that letter. You now have", warnings, "warnings left:", get_guessed_word(secret_word, letters_guessed))
            
            # If guessed letter is indeed in secret word
            elif guessed_char in secret_word:
                letters_guessed += guessed_char
                print('Good guess:', get_guessed_word(secret_word, letters_guessed))
            
            # If guessed letter is not in secret word
            else:
                letters_guessed += guessed_char
                if guessed_char in vowels:
                    guesses -= 1
                guesses -= 1
                print("Oops! This character is not in my word:", get_guessed_word(secret_word, letters_guessed))

    # Print out result and terminate
    score = guesses * len(set(secret_word))
    print('Congratulations, you won!')
    print('Your total score for this game is:', score)
    return None

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------

# Matching words with gaps
def match_with_gaps(my_word, secret_word):
    # Clean up the spaces
    word = my_word.replace(' ', '')

    # Check length
    if len(word) != len(secret_word):
        return False

    # Now check char by char, ignore unknown case of course
    for i in range(len(word)):
        if word[i] == '_':
            pass
        elif word[i] != secret_word[i]:
            return False

    # If pass all above comparision, return true
    return True

# Test cases, just chilling here
# print(match_with_gaps(" t e _ t ", "tact"))
# print(match_with_gaps(" a _ _ l e ", "banana"))
# print(match_with_gaps(" a _ _ l e ", "apple"))
# print(match_with_gaps(" a _ p l e ", "apple"))

# Searching through the word database to find suggestions
def show_possible_matches(my_word):
    # Clean up the spaces
    word = my_word.replace(' ', '')

    # Suggestion words and counts, cap at 20 for now
    suggestions = ''
    cnt = 0

    # Iterating through the word database to look for suggestions
    for char in wordlist:
        if match_with_gaps(word, char):
            suggestions += (char + ' ')
            cnt += 1
            if (cnt >= 20):
                return suggestions

    # Display result and terminate
    if (cnt == 0):
        print('No matches found')
        return None
    else:
        return suggestions

# Leaving 'em chilling
# print(show_possible_matches(" t _ _ t "))
# print(show_possible_matches(" a b b b b _ "))
# print(show_possible_matches(" a _ p l _ "))

# Easier version of hangman, supposedly
def hangman_with_hints(secret_word):
    # Setup some variables to store the game parameters
    warnings = 3
    guesses = 6
    letters_guessed = ''
    vowels = 'aeiou'

    # Welcome text
    print('Welcome to the game Hangman')
    print('I am thinking of a word that is', len(secret_word), 'letters long:', get_guessed_word(secret_word, letters_guessed))

    # Game start
    while not is_word_guessed(secret_word, letters_guessed):
        # End game if the player ran out of guesses
        print('----------------')
        if (guesses == 0):
            print('Sorry, you ran out of guesses. The word was:', secret_word)
            return None

        # Information prompting
        available_letters = get_available_letters(letters_guessed)
        print('You have', guesses, 'guesses left.')
        print('Available letters:', available_letters)
        guessed_char = str.lower(input('Please guess a letter: '))
        
        # Check for valid input first
        if (len(guessed_char) != 1) or (guessed_char not in string.ascii_lowercase):
            if guessed_char == '*':
                print('Possible word matches are:\n', show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
                pass
            else:
                if warnings:
                    warnings -= 1
                else:
                    guesses -= 1
                print('Oops! That is not a valid letter. You have', warnings, 'warnings left:', get_guessed_word(secret_word, letters_guessed))
        
        # Check for input char next
        else:
            # Check for already guessed letter
            if guessed_char in letters_guessed:
                if warnings:
                    warnings -= 1
                else:
                    guesses -= 1
                print("Oops! You've already guessed that letter. You now have", warnings, "warnings left:", get_guessed_word(secret_word, letters_guessed))
            
            # If guessed letter is indeed in secret word
            elif guessed_char in secret_word:
                letters_guessed += guessed_char
                print('Good guess:', get_guessed_word(secret_word, letters_guessed))
            
            # If guessed letter is not in secret word
            else:
                letters_guessed += guessed_char
                if guessed_char in vowels:
                    guesses -= 1
                guesses -= 1
                print("Oops! This character is not in my word:", get_guessed_word(secret_word, letters_guessed))

    # Print out result and terminate
    score = guesses * len(set(secret_word))
    print('Congratulations, you won!')
    print('Your total score for this game is:', score)
    return None



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # secret_word = 'apple'
    # hangman(secret_word)
    # pass

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
