x = int(input("Please enter exam result: "))

if x < 101 and x > 89 and x == 100:
	print("A")
elif x <= 89 and x >= 80: 
	print("B")
elif x <= 79 and x >= 60:
	print("C")
elif x <= 59 and x >= 50: 
	print("D")
elif x <= 49:
	print("F")
else:
	print("Not specified")