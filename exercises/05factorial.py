# Write a method to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1
#
# Example method call
#
# factorial(5)
#
# > 120
#


def factorial(n):
	new_num = 1
	while n > 0:
		new_num = new_num * n
		n -= 1
	print (new_num)
	

factorial(5)