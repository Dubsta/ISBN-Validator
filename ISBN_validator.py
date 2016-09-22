'''
ISBN validator
by Michael Atkinson
For Reddit sub:
r/DailyProgrammer challenge #197:Easy
'''

import re

print "\n"*2

print "What is your ISBN?"
isbn = raw_input()
isbn = isbn.replace("-","") 	# remove -
isbn = isbn.replace(" ","") 	# remove whitespace

#complile regex expressions
type10 = re.compile(r"^\d{10}$") # 10 digit
type10x = re.compile(r"^\d{9}X$") # 9 digit with X
type13 = re.compile(r"^\d{13}$") # 13 digit

success = "ISBN is valid!"
fail = "ISBN is invalid."

#10 digit ISBN logic
if type10.match(isbn) or type10x.match(isbn):
	factor = len(isbn)
	total = 0
	for digit in isbn:
		if digit == "X": 
			digit = 10
		total += (int(digit)*factor)
		factor -= 1
	if total % 11 == 0 :
		print success
	else:
		print fail

#13 digit ISBN logic
elif type13.match(isbn):
	total = 0
	counter = 1
	for digit in isbn:
		digit = int(digit)
		if counter % 2 == 0:
			digit = digit * 3
		counter += 1
		total += digit
	if total % 10 == 0 :
		print success
	else:
		print fail
else:  #neither 10 nor 13 digits
	print fail

print "\n"*2
