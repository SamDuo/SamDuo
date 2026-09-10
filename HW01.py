# You are required to complete the missing bodies of the functions below.

# A few tips:
# - Make sure you return the right value and datatype
# - Test your code for each function by uncommenting the respective test cases
# 	in the if __name__ == '__main__' block
# - Do not import modules within functions
# - Do not leave any print statements within your functions
# - Do not define functions within functions
# - Please replace the pass statements with your code
# - Submit in Gradescope as HW01.py - Your submission should be named exactly HW01.py


def welcome(welcome_str):
	"""
	Question 1

	Michael wants to say welcome to all the new students, but the string he wanted to use got mixed up 
	with some other words. Write a function that takes in a string as input and returns a string with 
	only every other word from the original string (including the first word, so 1,3,5,...). Finally, 
	add 5 exclamation marks to the end because you're so excited for the class.
	
	NOTE: THIS MUST BE DONE IN ONE LINE

	Args:
		welcome_str (string)
	Returns:
		string

	>>> print(welcome("Welcome hello to my CS name 2316 is"))
 
	Welcome to CS 2316!!!!!

	"""
	# split on whitespace to get the words, slice with a step of 2 to keep
	# indices 0, 2, 4, ... then put the spaces back with join
	return " ".join(welcome_str.split()[::2]) + "!!!!!"


if __name__ == '__main__':
	# Question 1
	print(welcome("Welcome hello to my CS name 2316 is"))
