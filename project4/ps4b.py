# Problem Set 4B
# Name: Hoang Nguyen
# Time Spent: 1:30

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    # Init class, holds input text and list of valid words
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    # Getter for message text
    def get_message_text(self):
        return self.message_text

    # Getter for valid words
    def get_valid_words(self):
        return list(self.valid_words)

    # Return a dictionary foor cipher message
    def build_shift_dict(self, shift):

        # For return
        shift_dict = {}

        # Cipher lower and upper case simultanously
        for i in range(len(string.ascii_lowercase)):
            cipher = (i + shift) % 26
            shift_dict[string.ascii_lowercase[i]] = string.ascii_lowercase[cipher]
            shift_dict[string.ascii_uppercase[i]] = string.ascii_uppercase[cipher]

        # Return and terminate
        return shift_dict

    # Applying the shift cipher to the current message text
    def apply_shift(self, shift):

        # Vaiables for return and conding
        cipher_string = ''
        shift_dict = self.build_shift_dict(shift)

        # Start encoding
        for char in self.message_text:
            cond = shift_dict.get(char, 0)
            if cond:
                cipher_string += cond
            else:
                cipher_string += char

        # Return and terminate
        return cipher_string

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        # Init class, inherit from message then create encryption
        # library, direction and message
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    # Getter for shift value
    def get_shift(self):
        return self.shift

    # Getter for encryption dictionary generated from shift value
    def get_encryption_dict(self):
        return dict(self.encryption_dict)

    # Getter for encrypted text
    def get_message_text_encrypted(self):
        return self.message_text_encrypted

    # Setter to change set shift value, also rebuilt dictionary
    # and encrypted message
    def change_shift(self, shift):
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)


class CiphertextMessage(Message):
    # Class initialize, basically take everything from message
    def __init__(self, text):
        Message.__init__(self, text)

    # Brute force decryption
    def decrypt_message(self):
        # Variable to store the best shift value and result
        best_shift = 0
        best = 0

        # Basically iterate through all 26 possible shift values (0-25)
        for i in range(0,26):
            itr_count = 0
            shift_search = self.apply_shift(i).lower().split(" ")

            # Clean up the split list first
            for word in shift_search:
                if is_word(self.valid_words, word):
                    itr_count += 1

            # Storing our result here
            if itr_count > best:
                best = itr_count
                best_shift = i

            # Break out if we have matched every word
            if best == len(shift_search):
                break

        # Return the decrypted message and terminate
        return self.apply_shift(best_shift)

if __name__ == '__main__':

    # # Test 1 for PlaintextMessage class
    # test1 = PlaintextMessage(string.ascii_lowercase, 12)
    # print(test1.get_message_text_encrypted())
    # test1.change_shift(-1)
    # print(test1.get_message_text_encrypted())

    # # Test 2 for PlaintextMessage class
    # text2 = 'mnopqrstuvwxyzabcdefghijkl'
    # test2 = PlaintextMessage(text2, -12)
    # print(test2.get_message_text_encrypted())

    # # Test 3 for PlaintextMessage ckass
    # text3 = '“Stop!” he yelled. “You’ve got two flat tires!”'
    # test3 = PlaintextMessage(text3, 4)
    # print(test3.get_message_text_encrypted())

    # Test 4 for CiphertextMessage class
    test4 = CiphertextMessage(get_story_string())
    print(test4.decrypt_message())
    
