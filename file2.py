import sys
i = ''
n = input()
m = 0
i = 0
array = []
main = []

for i in range(0, n):
	inp = raw_input()
	array(inp.split())
	main[array[0]] = array[1]

for i in range(0, n):
	take = raw_input()
	if take in main:
		print (take + " = " + main[take])
	else:
		print("404")
