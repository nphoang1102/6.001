# 
# Guessing and approximation algorithm from lecture 3
# with some twists on breaking condition to reduce
# guessing time. However code will break under negative input
# 
# - Hoang N -

# Define main function
def main():
   # Layout some constants and variables first
   epsilon = 0.1
   guess = 0.0
   increment = 0.01
   last_approximation = 0.0
   num_guesses = 0

   # Prompt user for input
   cube = int(input('Input cube: '))

   # Start guessing with approximation using epsilon
   while abs(guess**3 - cube) >= epsilon:
      guess += increment
      num_guesses += 1

      # Improved breaking condition compared to the guess <= cube
      if (last_approximation) and (last_approximation <= abs(guess**3 - cube)):
         break
      last_approximation = abs(guess**3 - cube)

   # Display result and terminate
   print('Total guess time is', num_guesses)
   if abs(guess**3 - cube) >= epsilon:
      print('Failed to find root of', cube)
      print('Closest approximation is', guess)
   else:
      print(guess, 'is the closest to the cube root of', cube)
   return None

# Invoke main
main()
