'''
ISBN validator
by Michael Atkinson
Reddit daily challenge #197

'''


import re

print "\n"*2

print "What is your ISBN?"
isbn = raw_input()
isbn = isbn.replace("-","") 	# remove -
type10 = re.compile(r"^\d{10}$") # 10 digit
type10x = re.compile(r"^\d{9}X$") # 9 digit with X
type13 = re.compile(r"^\d{13}$") # 13 digit

success = "ISBN is valid!"
fail = "ISBN is invalid."

if type10.match(isbn) or type10x.match(isbn):
	print "type 10" #debugging
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

elif type13.match(isbn):
	print "type 13" #debugging
	total = 0
	oddEven = 1
	for digit in isbn:
		digit = int(digit)
		if oddEven % 2 == 0:
			digit = digit * 3
		oddEven += 1
		total += digit
		print digit #debugging
	if total % 10 == 0 :
		print success
	else:
		print fail


else:
	print fail


print "\n"*2
