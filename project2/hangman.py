# Problem Set 2, hangman.py
# Name: Hoang N
# Time spent: 85 mins

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
            print('Oops! That is not a valid letter. You have', warnings, 'left:', get_guessed_word(secret_word, letters_guessed))
        
        # Check for input char next
        else:
            # Check for already guessed letter
            if guessed_char in letters_guessed:
                if guessed_char not in secret_word:
                    if warnings:
                        warnings -= 1
                    else:
                        guesses -= 1
                print("Oops! You've already guessed that letter. You now have", warnings, "warnings")
            
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



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    # secret_word = 'apple'
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
