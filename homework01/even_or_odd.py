# The following function determines if a number is even or
# odd and prints out the number with its description
def even_or_odd(numList):
	for x in numList:
		# If the remainder of the division by 2 is equal to 0,
		# then the number is even
		if ((x % 2) == 0):
			print(x, "is even.")
		# If the remainder is not equal to 0, then the number
		# is odd
		else:
			print(x, "is odd.")

# This program determines if the numbers of a given
# list are even or odd and prints it out.
num_list = [10, 5, 40, 37, 60, 110, 63, 48, 1, 89]
even_or_odd(num_list)
