import string

def func(input):
    # Some storage variables
    cleaned = ''
    last_char = ''

    # Start with lower case, then strip off punctuations
    # and excessive space
    lower = input.lower()
    for char in lower:
        cond = char == ' ' and last_char != ' '
        if ((char not in string.punctuation) and (char != ' ')) or (cond):
            cleaned += char
        last_char = char

    # Return cleaned string and termintate
    return cleaned

if __name__ == "__main__":
    print(func("~pu!RPle@#     $%cow'"))