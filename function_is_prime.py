def main():
    give = int(input("Enter a number, to see if it is prime or not: "))
    is_prime(give)


def is_prime(integer):
    # the accumulator starts as 2, because 2 is the first number that is greater than 1.
    i = 2
    # We also initialize the value at true, so if the number below fails the if statement
    # in the while loop, it will not be changed from True to False, and therefore remains prime
	
    val = True
    

    # These if statements take care of the cases of a 0 or a 1 
    if integer == 0:
	    val = False
	    return val
    if integer == 1:
	    val = False
	    return val

    # While i < integer, test if it's divisible by anything
    while i < integer:
	    if integer % i == 0:
		    val = False
		    print("This number is NOT prime.")
		    return val
	    # This loop continues until i >= integer
	    i = i + 1
    # If after the while loop has been satisfied and val still is True;
    # return True!
    if val == True:
            print("This number is prime!!!")
    return val

main()
