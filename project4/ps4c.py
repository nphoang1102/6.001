# Problem Set 4C
# Name: Hoang Nguyen
# Time Spent: 1:10

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    # print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    # print("  ", len(wordlist), "words loaded.")
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


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):

    # Class init, holding the message text and list of valid words
    def __init__(self, text):
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    # Return the original message text
    def get_message_text(self):
        return self.message_text

    # Return a clone list of valid words in case anyone tinker with it
    def get_valid_words(self):
        return list(self.valid_words)
    
    # Build our substitution dictionary based on the input vowels permutation
    def build_transpose_dict(self, vowels_permutation):
        
        # Dictionary for return
        vowel_map = {}

        # Start iterating through the permutation and substitute for vowels
        for i in range(len(vowels_permutation)):
            vowel_map[VOWELS_LOWER[i]] = vowels_permutation[i].lower()
            vowel_map[VOWELS_UPPER[i]] = vowels_permutation[i].upper()

        # Put in consonants
        for char in CONSONANTS_LOWER:
            vowel_map[char] = char
            vowel_map[char.upper()] = char.upper()

        # Return dictionary and terminate function
        return vowel_map

    # Apply the substitution based on the input dictionary
    def apply_transpose(self, transpose_dict):
        # Vaiables for return
        cipher_string = ''

        # Start encoding
        for char in self.message_text:
            cond = transpose_dict.get(char, 0)
            if cond:
                cipher_string += cond
            else:
                cipher_string += char

        # Return and terminate
        return cipher_string
        
class EncryptedSubMessage(SubMessage):
    # Init function
    def __init__(self, text):
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        # Variables to store decrypt result and permutation list
        best_score = 0
        best_permutation = ''
        permutation_list = get_permutations(VOWELS_LOWER)
        # print('Permutation list:', permutation_list, '| List length:', len(permutation_list))

        # Start going through the permutation list and decrypt
        for e in permutation_list:
            # Score tracking and get the iteration message
            itr_score = 0
            message = self.apply_transpose(self.build_transpose_dict(e)).split(" ")
            
            # Start scoring
            for char in message:
                if is_word(self.valid_words, char):
                    itr_score += 1

            # Update best score by far
            if itr_score > best_score:
                best_score = itr_score
                best_permutation = e

        # Now use best permutation found to decrypt the message, if found any
        if best_score:
            return self.apply_transpose(self.build_transpose_dict(best_permutation))

        # Else just keep the message as is
        else:
            return self.get_message_text()

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    # Test 1:
    text1 = SubMessage("On the first day of Januray, he marks the begin of a new year, 'the year of Changes'.")
    perm1 = "ieoua"
    dict1 = text1.build_transpose_dict(perm1)
    print("Original message:", text1.get_message_text(), "Permutation:", perm1)
    print("Expected encryption:", "Un the forst diy uf Jinariy, he mirks the begon uf i new yeir, 'the yeir uf Chinges'.")
    print("Actual encryption:", text1.apply_transpose(dict1))
    enc_text1 = EncryptedSubMessage(text1.apply_transpose(dict1))
    print("Decrypted message:", enc_text1.decrypt_message())

    # Test 2:
    text2 = SubMessage('Mister Owl has just woke up, from his long nap.')
    perm2 = "oeuai"
    dict2 = text2.build_transpose_dict(perm2)
    print("Original message:", text2.get_message_text(), "Permutation:", perm2)
    print("Expected encryption:", 'Muster Awl hos jist wake ip, fram hus lang nop.')
    print("Actual encryption:", text2.apply_transpose(dict2))
    enc_text2 = EncryptedSubMessage(text2.apply_transpose(dict2))
    print("Decrypted message:", enc_text2.decrypt_message())