'''
ISBN validator
by Michael Atkinson
Reddit daily challenge #197

'''


\import re

print "\n"*2

print "What is your 10 digit ISBN?"
isbn = raw_input()
isbn = isbn.replace("-","") 	# remove -
type1 = re.compile(r"^\d{10}$") # 10 digit
type2 = re.compile(r"^\d{9}X$") # 9 digit with X


if type1.match(isbn) or type2.match(isbn):
	factor = len(isbn)
	total = 0
	for digit in isbn:
		if digit == "X": 
			digit = 10
		total += (int(digit)*factor)
		factor -= 1
	if total % 11 == 0 :
		print "ISBN looks good!"
	else:
		print "ISBN seems bad."
else:
	print "Please enter a valid 10 digit ISBN."


print "\n"*2
