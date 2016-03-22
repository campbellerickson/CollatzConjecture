print "Type '123' to start the program::",
check = input()


if check == 123:


	print "To what number would you like to prove the Collatz Conejecture?::"
	limit = input()
	int(limit)
	
	for x in xrange(1,limit+1):
		num=x
		original=x
		iterations=0

		while num > 1:
			if (num % 2 == 0):
				num = num/2
				iterations = iterations + 1
			elif (num % 2 != 0): 
				num = (num * 3) + 1
				iterations = iterations + 1

		

		print original, "is proven through", iterations, "iterations."
			

	print "The Collatz Conjecture is proven!" 

