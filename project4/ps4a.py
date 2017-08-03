# Problem Set 4A
# Name: Hoang Nguyen
# Collaborators:
# Time Spent: 1:00

def get_permutations(sequence):
    # The return list
    permu = list()

    # Base case of one character
    if len(sequence) <= 1:
        permu.append(sequence)

    # Recursive here
    else:
        # recursively take the head and permutate the body
        body = sequence[1:]
        list_body = get_permutations(body)

        # Then put the head into different position in the body
        for char in list_body:
            for i in range(len(char) + 1):
                permu.append(char[0:i] + sequence[0] + char[i:])

    # Return result here
    return permu


if __name__ == '__main__':

    #EXAMPLE 1
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
    #EXAMPLE 2
    example_input = 'ef'
    print('Input:', example_input)
    print('Expected Output:', ['ef', 'fe'])
    print('Actual Output:', get_permutations(example_input))

    #EXAMPLE 3
    example_input = 'bat'
    print('Input:', example_input)
    print('Expected Output:', ['bat', 'bta', 'abt', 'atb', 'tba', 'tab'])
    print('Actual Output:', get_permutations(example_input))

