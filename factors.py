print('The factors of the number you type when prompted will be displayed')
a = int(input('Type here: // '))
b = a
while b > 0:
	if a % b == 0:
		print(b)
	b -= 1
