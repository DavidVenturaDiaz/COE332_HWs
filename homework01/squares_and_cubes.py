# The following function returns a list with the squares
# of a list received as the argument
def squared(numList):
	squaredNumList = []
	for x in numList:
		#Square the current number and add it to new list
		squaredNumList.append(x*x)
	return squaredNumList

# The following function returns a list with the cubes
# of a list received as the argument
def cubed(numList):
	cubedNumList = []
	for x in numList:
		#Cube the current number and add it to new list
		cubedNumList.append(x*x*x)
	return cubedNumList

# The following program obtains the squares and cubes of a given list
# that contains numbers. All three lists are printed out side-by-side
# in three columns
num_list = [1,2,3,4,5,6,7,8,9,10]
squared_num_list = squared(num_list)
cubed_num_list = cubed(num_list)
for x in range(0,10):
	print(num_list[x], squared_num_list[x], cubed_num_list[x])

