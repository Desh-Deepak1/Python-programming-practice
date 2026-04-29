n=int(input("Enter a Number:-"))
fact=1
if(n<0):
	print("Factorial dose not EXIT for negative numbers")
elif n==0:
	print("The Factorial of 0 is 1")
else:
	for i in range(1, n+1):
		fact*=i
	print(f"The FACTORIAL of {n} is {fact}")
