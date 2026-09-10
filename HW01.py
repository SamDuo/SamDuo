from pprint import pprint



# CS 2316 - Fall 2026 - HW01 Python Fundamentals
# HW01: This homework is due by {Wednesday 9/9} @ 11:59PM through Gradescope

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
	# split into words, step by 2 to keep indices 0, 2, 4, ... then put the spaces back
	return " ".join(welcome_str.split()[::2]) + "!!!!!"


def email_search(email_A, email_B):
	"""
	Question 2

	You received two separate emails from Georgia Tech and want to know which characters are used in at 
	least one of them. Write a function that takes in both emails as strings and returns a sorted list 
	of all of the unique characters that appear in at least one email. 

	NOTE: THIS MUST BE DONE IN ONE LINE

	Args:
		email_A (string)
		email_B (string)
	Returns:
		list of strings

	>>> print(email_search("Hello", "Goodbye"))
 
	['G', 'H', 'b', 'd', 'e', 'l', 'o', 'y']

	"""
	# glue the two emails together, cast to a set to drop the duplicates, then sort
	return sorted(set(email_A + email_B))


def gt_football_record(record):
	"""
	Question 3

	Currently, Georgia Tech football records are stored in the following format: "firstname lastname|position".
	Write a function that takes in a football record string and returns a string in the following format: 
	"LASTNAME, FIRSTNAME - POSITION". Note that the last name, first name, and position should all be 
	uppercase in the final string. Do NOT hardcode your solution.

	NOTE: THIS MUST BE DONE IN ONE LINE, you may not use for or while loops

	Args:
		record (string)
	Returns:
		string

	>>> print(gt_football_record("haynes king|quarterback"))
 
	KING, HAYNES - QUARTERBACK

	"""
	# split on the | to separate the name from the position, then split the name on whitespace
	return f"{record.split('|')[0].split()[1].upper()}, {record.split('|')[0].split()[0].upper()} - {record.split('|')[1].upper()}"
	

def extra_credit(students_grades):
	"""
	Question 4 

	A professor is trying to decide if she wants to give an extra credit assigment for her class. She wants 
	to figure out if the exam average is at least 75. If it is, she will decide that the class doesn't need 
	extra credit. Write a function that takes in a dictionary with students' names as the keys and their exam 
	grades as the values. Return True if theaverage is less than 75. Otherwise, return False.
	
	NOTE: THIS MUST BE DONE IN ONE LINE

	Args:
		students_grades (dict)
	Returns:
		bool
	
	>>> print(extra_credit({"Buzz" : 65, "George P" : 81, "Haynes King" : 90}))
	
	False
	
	"""

	# .values() gives just the grades, so the average is the sum over the number of students
	return sum(students_grades.values()) / len(students_grades) < 75


def prereq_check(records):
	"""
	Question 5
	It's registration season, and the CS advising office is swamped. Before letting students register for CS 
	2316 or CS 4400, you need to make sure they've survived CS 1301 first. You're given a list of records, 
	each formatted as 'STUDENT COURSE' (e.g. 'Aditi CS1301'). Find every record for CS1301 and return a list 
	of just the student names, sorted alphabetically.

	NOTE: THIS MUST BE DONE IN ONE LINE

	Args:
		records (list)
	Returns:
		list of strings

	>>> print(prereq_check(['Lisa CS1301', 'Tim CS2316', 'Alex CS1301', 'Brianna CS4400']))
	['Alex', 'Lisa']

	"""
	# keep the first word of a record only when the second word is the prereq
	return sorted([record.split()[0] for record in records if record.split()[1] == "CS1301"])


def dorm_dict(dorms):
	"""
    Question 6

	You have a list of dorms and their locations of the form "dorm-location". To make life easier, you want 
	to convert this list to a dictionary. Write a function that takes in this list and returns a dictionary 
	of the form {dorm: location}.
	
	NOTE: THIS MUST BE DONE IN ONE LINE

	Args:
		dorms (list)
	Returns:
		dict

	>>> print(dorms_dict(["Armstrong-West", "Brown-East", "Field-East", "Caldwell-West", "Folk-West", "Glenn-East", "Perry-East"]))
 
	{'Armstrong': 'West', 'Brown': 'East', 'Field': 'East', 'Caldwell': 'West', 'Folk': 'West', 'Glenn': 'East', 'Perry': 'East'}
 
    """
	# splitting on the hyphen gives a 2 item list, which casts straight to a dictionary
	return dict([dorm.split("-") for dorm in dorms])


def course_schedule(department, course_numbers):
	"""
	Question 7

	You are trying to determine what your schedule should look like next semester. As an industrial and 
	systems engineering student, you know that there are many classes in many different departments offered 
	to you. You have two lists: one of departments and one of course numbers. The items correspond, so the first 
	items in each list together form a course that you could take (i.e. department[0] is "APPH" and course_numbers[0] 
	is 1040, so you could take APPH 1040). You are only interested in taking courses that fit the following criteria:
	- the department code is 4 letters long
	- the course number doesn't end in a 0 
	Return a list of all of the courses you will take next semester with the course number and department as a tuple. 
	Sort the classes by the course department.

	NOTE: THIS MUST BE DONE IN ONE LINE

	Args:
		department (list)
		course_numbers (list)
	Returns:
		list of tuples

	>>> print(course_schedule(["APPH", "ISYE", "CS", "ISYE", "CS", "ISYE", "ACCT", "MATH"], [1040, 2027, 4400, 3232, 2316, 3044, 2101, 2551]))
 	
	[(2101, 'ACCT'), (2027, 'ISYE'), (3232, 'ISYE'), (3044, 'ISYE'), (2551, 'MATH')]

	"""
	# zip pairs each department with its course number, then sort the survivors on the department
	return sorted([(num, dept) for dept, num in zip(department, course_numbers) if len(dept) == 4 and num % 10 != 0], key=lambda course: course[1])


def decor_list(price_list, spot_list):
	"""
	Question 8

	Eli just moved into his dorm which is soulless and devoid of anything Georgia Tech. He made two lists of 
	his favorite decor. The first is a list of tuples with the decor name and price, and the second is a list 
	of tuples with the decor name and the best spot for the decor. The lists are in the same order and contain 
	the same items, so the first item in each list is the same, but each list contains different information. 
	Eli only wants decor that fits the following criteria: 
	- it costs less than 10 dollars 
	- it covers up locations starting with the letter "B" (because he hates the Georgia "B"***dogs) 
	That is, he will buy all of the decor that is less than 10 dollars and goes in a location that starts with 
	the letter "B". Write a function that takes the price_list and spot_list and returns a list of decor names 
	that satisfy both conditions. Additionally, sort this new list in alphabetical order.

	NOTE: THIS MUST BE DONE IN ONE LINE

	Args:
		price_list (list of tuples)
		spot_list (list of tuples)
	Returns:
		list of strings
	
	>>> print(decor_list([("GT Pillow", 5), ("Ramblin Reck Lamp", 18), ("Yellow Jacket Plushie", 7), ("Bobby Dodd Turf", 0)],
	[("GT Pillow", "Bed"), ("Ramblin Reck Lamp", "Desk"), ("Yellow Jacket Plushie", "Banister"), ("Bobby Dodd Turf", "Floor")]))
	
	["GT Pillow", "Yellow Jacket Plushie"]

	"""

	# the lists line up, so zip them and check the price from one tuple and the spot from the other
	return sorted([price[0] for price, spot in zip(price_list, spot_list) if price[1] < 10 and spot[1][0] == "B"])


def total_score(football_scores_2025):
	"""
	Question 9

	Buzz is super excited for the 2026 football season and decided to reminisce on last season's home games. 
	Buzz has a list of tuples containing the name of the opposing school, the number of points Georgia Tech 
	scored, and the number of points scored by the other team. Buzz wants to calculate approximately how many 
	touchdowns were scored each home game. Return a list of tuples containing the name of the opposing school 
	in all caps and the approximate total number of touchdowns scored during the game, calculated by dividing 
	the total number of points scored by both teams by 7 and rounding down. The returned list should be sorted
	by approximate total touchdowns in descending order.
	
	NOTE: THIS MUST BE DONE IN ONE LINE

	Args:
		football_scores_2025 (list of tuples)
	Returns:
		list of tuples

	>>> football_scores_2025 = [("Gardner-Webb", 59, 12), ("Clemson", 24, 21), ("Temple", 45, 24), ("Virginia Tech", 35, 20), ("Syracuse", 41, 16), ("Pittsburgh", 28, 42), ("georgia", 9, 16)]
 	>>> pprint(total_score(football_scores_2025))

	[('GARDNER-WEBB', 10), ('PITTSBURGH', 10), ('TEMPLE', 9), ('SYRACRUSE', 8), ('VIRGINA TECH', 7), ('CLEMSON', 6), ('GEORGIA', 3)]

	"""

	# // is integer division, which rounds down for us, then sort on the touchdown count backwards
	return sorted([(school.upper(), (gt_points + other_points) // 7) for school, gt_points, other_points in football_scores_2025], key=lambda game: game[1], reverse=True)


def dining_sort(campus_dining):
	"""
	Question 10

	Anushka loves eating at the campus dining options but is trying to limit her spending. Given a list of 
	tuples containing campus dining locations and their average meal prices, create a dictionary with the 
	dining location names as the keys. The corresponding value for each key should be... 
	- "Expensive" if the price is greater than or equal to 20
	- "Cheap" if the price is less than or equal to 15
	- "Average" otherwise 
	However, if the dining location name is all lowercase, do not include it in the dictionary.

	NOTE: THIS MUST BE DONE IN ONE LINE

	Args:
		campus_dining (list)
	Returns:
		dict

	>>> campus_dining = [("Asian Fusion", 22), ("Chick-fil-A", 14), ("Tindrum", 18), ("subway", 11), ("West Village", 8), ("zoe's tacos", 7)]
	>>> print(dining_sort(campus_dining))
	{'Asian Fusion': 'Expensive',
	'Chick-fil-A': 'Cheap',
	'Tindrum': 'Average',
	'West Village': 'Cheap'}

	"""

	# the if at the end filters out the lowercase names, the conditional expression picks the label
	return {name: "Expensive" if price >= 20 else "Cheap" if price <= 15 else "Average" for name, price in campus_dining if not name.islower()}




if __name__ == "__main__":

	pass

	# print("Q1")
	# print(welcome("Welcome hello to my CS name 2316 is"))

	# print("Q2")
	# print(email_search("Hello", "Goodbye"))
	
	# print("Q3")
	# print(gt_football_record("haynes king|quarterback"))
	
	# print("Q4")
	# inventory = {"Buzz" : 65, "George P" : 81, "Haynes King" : 90}
	# print(extra_credit(inventory))

	# print("Q5")
	# print(prereq_check(['Lisa CS1301', 'Tim CS2316', 'Alex CS1301', 'Brianna CS4400']))

	# print("Q6")
	# print(dorm_dict(["Armstrong-West", "Brown-East", "Field-East", "Caldwell-West", "Folk-West", "Glenn-East", "Perry-East"]))

	# print("Q7")
	# print(course_schedule(["APPH", "ISYE", "CS", "ISYE", "CS", "ISYE", "ACCT", "MATH"], [1040, 2027, 4400, 3232, 2316, 3044, 2101, 2551]))

	# print("Q8")
	# print(decor_list([("GT Pillow", 5), ("Ramblin Reck Lamp", 18), ("Yellow Jacket Plushie", 7), ("Bobby Dodd Turf", 0)],[("GT Pillow", "Bed"), ("Ramblin Reck Lamp", "Desk"), ("Yellow Jacket Plushie", "Banister"), ("Bobby Dodd Turf", "Floor")]))

	# print("Q9")
	# football_scores_2025 = [("Gardner-Webb", 59, 12), ("Clemson", 24, 21), ("Temple", 45, 24), ("Virginia Tech", 35, 20), ("Syracuse", 41, 16), ("Pittsburgh", 28, 42), ("georgia", 9, 16)]
	# print(total_score(football_scores_2025))

	# print("Q10")
	# campus_dining = [("Asian Fusion", 22), ("Chick-fil-A", 14), ("Tindrum", 18), ("subway", 11), ("West Village", 8), ("zoe's tacos", 7)]
	# print(dining_sort(campus_dining))

