def q1(x, y):
	arr = []
	for z in range(x, y):
		if (z%7 == 0 and z%5 != 0):
			arr.append(str(z))
	return ','.join(arr)

def q2(x):
	if x == 0:
		return 1
	return x * level2(x-1)

def q3(n):
	d = {}
	for i in range(1, n+1):
		d[i] = i*i
	return d

def q4():
	inputString = input("Enter comma separated string > ").split(',')
	arr = []
	for num in inputString:
		arr.append(num)
	print(arr, tuple(arr), sep="\n")

class Q5(object):
	def __init__(self, inputString):
		self.inputString = inputString
	def getString(self):
		self.inputString = input("Enter a string > ")
	def printString(self):
		print(self.inputString.upper())

import math

def q6():
	C = 50
	H = 30
	D_string = input("Enter value(s) of D > ").split(',')
	results = []
	for D in D_string:
		results.append(str(math.floor(math.sqrt((2*C*int(D)/H)))))
	return ','.join(results)

def q7():
	X, Y = [int(num) for num in input("Enter numbers > ").split(',')]
	arr = [[i*j for j in range(0, Y)] for i in range(0, X)]
	return arr

def q8():
	words = [word for word in input("Enter comma separated list of words > ").split(',')]
	print(','.join(sorted(words)))

def q9():
	lines = []
	while True:
		input_sentence = input("Enter sentence > ").upper()
		if input_sentence:
			lines.append(input_sentence.upper())
		else:
			break
	for sentence in lines:
		print(sentence)

def q10():
	print(' '.join(sorted(set([word for word in input("Enter sentence > ").split()]))))

def q11():
	binary_input = [bin_word for bin_word in input("Enter binary numbers > ").split(',') if (int(bin_word, 2)%5 == 0)]
	print(','.join(binary_input))

def q12():
	lower, upper = [int(num) for num in input("Enter lower,upper > ").split(',')]
	results = []
	for num in range(lower, upper+1):
		isStillEven = False
		for digit in str(num):
			if int(digit)%2 == 0:
				isStillEven = True
			else:
				isStillEven = False
				break
		if isStillEven:
			results.append(str(num))
	print(','.join(results))

def main():
	q12()

if __name__ == "__main__":
	main()









