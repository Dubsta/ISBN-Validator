'''
 ibsn validator

Reddit daily challenge #197

Write a function that can return True if a nubmer is a valid ibsn.

*To do this.
- Multiply by factor of 10 decrementing each time.
- add result to total
-after loop finished total % 11--> if 0 True else False

'''
import re

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
