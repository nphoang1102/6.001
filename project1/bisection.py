#
# Bisection search to guess and check from lecture 3. Code
# still break under negative input and numbers from 0 to 1
# 

# Define main function
def main():
   # Put down some constants and storing variables first
   epsilon = 0.01
   num_guesses = 0
   low = 0

   # Prompting user for input and do some initial calculations
   cube = int(input('Input cube: '))
   high = cube
   guess = (high + low)/2.0

   # Start guessing with approximation using bisection search algorithm
   while abs(guess**3 - cube) >= epsilon:
      if guess**3 < cube:
         low = guess
      else:
         high = guess
      guess = (high + low)/2.0
      num_guesses += 1

   # Display result and terminate
   print('Total guess time is', num_guesses)
   print(guess, 'is close to the cube root of', cube)
   return None

# Invoke main
main()