# Problem Set 4A
# Name: Hoang Nguyen
# Collaborators:
# Time Spent: 1:00

def get_permutations(sequence):
    permu = list()
    if len(sequence) <= 1:
        permu.append(sequence)
    else:
        body = sequence[1:]
        list_body = get_permutations(body)
        for char in list_body:
            for i in range(len(char) + 1):
                permu.append(char[0:i] + sequence[0] + char[i:])
    return permu

    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    pass #delete this line and replace with your code here

if __name__ == '__main__':
    print(get_permutations('abc'))
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    # pass #delete this line and replace with your code here

