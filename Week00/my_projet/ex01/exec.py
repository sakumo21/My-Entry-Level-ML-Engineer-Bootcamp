import sys

i = len(sys.argv) - 1

if i > 0:
	while i > 0:
		y = len(sys.argv[i])
		while y > 0:
			if sys.argv[i][y - 1].islower():
				print(sys.argv[i][y - 1].upper(), end="")
			elif sys.argv[i][y - 1].isupper():
				print(sys.argv[i][y - 1].lower(), end="")
			else:
				print(sys.argv[i][y - 1], end="")
			y -= 1
		print(" ", end="")
		i -= 1
	print("")