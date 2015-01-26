'''
ISBN validator function
by Michael Atkinson
r/DailyProgrammer challenge #197:easy

'''

def isbn_validate(isbn):
	"""Takes an ISBN (MUST BE STRING) as argument and returns True or False."""
	isbn = str(isbn) #To stop crashing on non-strings
	isbn = isbn.replace("-","") #remove -
	import re
	type10 = re.compile(r"^\d{10}$") # 10 digit
	type10x = re.compile(r"^\d{9}X$") # 9 digit with X
	type13 = re.compile(r"^\d{13}$") # 13 digit
	print isbn #Debugging

	if type10.match(isbn) or type10x.match(isbn): #10 digit
		print "10 digit" #Debugging
		factor = len(isbn)
		total = 0
		for digit in isbn:
			if digit == "X": 
				digit = 10
			total += (int(digit)*factor)
			factor -= 1
		if total % 11 == 0 :
			print "success"	
			return True
		else:
			print "fail"
			return False

	elif type13.match(isbn): #13 digit
		print "13 digit" #debug
		total = 0
		counter = 1
		for digit in isbn:
			digit = int(digit)
			if counter % 2 == 0:
				digit = digit * 3
			counter += 1
			total += digit
		if total % 10 == 0 :
			print "success"
			return True
		else:
			print "fail"
			return False
	else:  #neither 10 nor 13 digits
		print "null" #debug
		print "fail"
		return False
#end function

test13 = "978-3-16-148410-0"
test10x = "0-8044-2957-X"
test10 = "99921-58-10-7"
failer = 1.234324
isbn_validate(failer)
