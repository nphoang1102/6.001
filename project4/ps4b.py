# Problem Set 4B
# Name: Hoang Nguyen
# Time Spent: 45

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

        # Cipher upper case first
        for i in range(len(string.ascii_uppercase)):
            cipher = i + shift
            if (cipher > 25):
                cipher -= 26
            shift_dict[string.ascii_uppercase[i]] = string.ascii_uppercase[cipher]

        # Then cipher lower case
        for i in range(len(string.ascii_lowercase)):
            cipher = i + shift
            if (cipher > 25):
                cipher -= 26
            shift_dict[string.ascii_lowercase[i]] = string.ascii_lowercase[cipher]

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
    def __init__(self, text):
        Message.__init__(self, text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        pass #delete this line and replace with your code here

if __name__ == '__main__':

    test = PlaintextMessage(get_story_string(), 1)
    print(test.get_message_text_encrypted())
    test.change_shift(-3)
    print('New story man')
    print(test.get_message_text_encrypted())

#    #Example test case (PlaintextMessage)
#    plaintext = PlaintextMessage('hello', 2)
#    print('Expected Output: jgnnq')
#    print('Actual Output:', plaintext.get_message_text_encrypted())
#
#    #Example test case (CiphertextMessage)
#    ciphertext = CiphertextMessage('jgnnq')
#    print('Expected Output:', (24, 'hello'))
#    print('Actual Output:', ciphertext.decrypt_message())

    #TODO: WRITE YOUR TEST CASES HERE

    #TODO: best shift value and unencrypted story 
    
