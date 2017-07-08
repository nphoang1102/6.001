# Importing library to do logarithmatic
from numpy import log2

def main():
	# Input is read in as a strin, thus need casting
	x = int(input("Enter number x: "))
	y = int(input("Enter number y: "))

	# Comput computation here and printout to screen
	print("x**y = ", str(x**y))
	print("log(x) = ", str(log2(x)))

	# Done
	return

# Invoke main
main()
