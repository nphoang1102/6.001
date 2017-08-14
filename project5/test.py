import string
from datetime import datetime
import pytz
import time

def clean_up_text(input):

    # Clean up the input by converting to lower case first
    lower = input.lower()

    # First convert all punctuations to spaces
    converted_to_space = ''
    for char in lower:
        if char in string.punctuation:
            converted_to_space += ' '
        else:
            converted_to_space += char

    # Next remove excessive space
    cleaned = ''
    last_char = ''
    for char in converted_to_space:
        if ((char == ' ') and (last_char != ' ') and (last_char != '')) or (char != ' '):
            cleaned += char
        last_char = char

    # Return cleaned string and termintate
    return cleaned

def is_phrase_valid(input):

    # Some storage variables
    cleaned = ''
    last_char = ''

    # Convert the input to all lower case first,
    # then check for excessive space and punctuations
    lower = input.lower()
    for char in lower:
        cond = char == ' ' and last_char == ' '
        if (char in string.punctuation) or (cond):
            return False
        last_char = char

    # Terminate and return true if we have not yet terminated
    return True

def time_test(input_time):
    # Setup the standard time format
    time_format = "%d %b %Y %H:%M:%S"
    time = datetime.strptime(input_time, time_format)
    ancient = datetime(1987, 10, 15)
    print('Evaluation result:', time > ancient)

def printS(s1, s2, s3):
    print(s1, s2, s3)

def addNum(n1, n2):
    print(n1+n2)

def dict_test(in_var):
    dict_map = {'print': printS, 'addNum': addNum}
    dict_map[in_var[0]](*in_var[1:])

if __name__ == "__main__":
    # print(clean_up_text("~puRPle@#     $%cow'"))
    # print(clean_up_text("~puRPle@#$%cow'"))
    # print("'purple cow???' validity:", is_phrase_valid('purple cow???'))
    # print("'purple    cow' validity:", is_phrase_valid('purple    cow'))
    # print("'mOoOoOoO' validity:", is_phrase_valid('mOoOoOoO'))
    # time_test('12 Oct 2016 23:59:59')
    dict_test(['print', 'What is this socery?', 'b', 'c'])