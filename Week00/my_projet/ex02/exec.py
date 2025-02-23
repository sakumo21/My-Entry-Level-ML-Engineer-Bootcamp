import sys

def check_isnum(s):
	if isinstance(s, (int, float)):
		return 1
	else:
		return 0


if __name__ == '__main__':
	i = len(sys.argv) - 1
	if i == 1:
		if sys.argv[1].isnumeric():
			if int(sys.argv[1]) == 0:
				print("I'm Zero.")
			elif int(sys.argv[1]) % 2 == 0:
				print("I'm Even.")
			else:
				print("I'm Odd.")
		else :
			print("argument is not an integer")
	elif i > 1:
		print("more than one argument is provided")