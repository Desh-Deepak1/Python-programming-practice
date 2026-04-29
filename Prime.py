num = int(input("Enter a Number :-"))
if num>1:
	for i in range(2,int(num**0.5)+1):
		if (num%i)==0:
			print("{num} is not a PRIME number")
			break
	else:
		print("{num} is a PRIME number")
else:
	print("{num} is not a PRIME number")
