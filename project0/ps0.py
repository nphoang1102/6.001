# Importing library to do logarithmatic
from numpy import log2

def main():
   # Input is read in as a strin, thus need casting
   x = int(input("Enter number x: "))
   y = int(input("Enter number y: "))

   # Comput computation here and printout to screen
   print("x**y =", (x**y))
   print("log(x) =", (log2(x)))
   # Does not require casting if using comma, pretty neat

   # Done
   return

# Invoke main
main()
