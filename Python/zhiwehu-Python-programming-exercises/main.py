def level1(x, y):
	arr = []
	for z in range(x, y):
		if (z%7 == 0 and z%5 != 0):
			arr.append(str(z))
	return ','.join(arr)

def level2(x):
	if x == 0:
		return 1
	return x * level2(x-1)

def level3(n):
	d = {}
	for i in range(1, n+1):
		d[i] = i*i
	return d

def level4():
	inputString = input("Enter comma separated string > ").split(',')
	arr = []
	for num in inputString:
		arr.append(num)
	print(arr, tuple(arr), sep="\n")

class Level5(object):
	def __init__(self, inputString):
		self.inputString = inputString
	def getString(self):
		self.inputString = input("Enter a string > ")
	def printString(self):
		print(self.inputString.upper())

def main():
	# print(level1(2000, 3200))
	# print(level2(int(input("Enter number > "))))
	# print(level3(int(input("Enter number > "))))
	# level4()
	l = Level5(input("Enter a string > "))
	l.getString()
	l.printString()

if __name__ == "__main__":
	main()









