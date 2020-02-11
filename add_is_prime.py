def main():
    print("This program will ask for a number")
    print("and will print the sum of all of the")
    print("first prime numbers up to the number given.")
    n = int(input("Please enter a number: "))
    
    i = 0
    count = 0
    total = 0
    while count < n:
        if is_prime(i):
            total += i
            count += 1
        i += 1
    print("The sum of the first ", n, " prime numbers is: ", total, sep='')


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
		    return val
	    # This loop continues until i >= integer
	    i = i + 1
    # If after the while loop has been satisfied and val still is True;
    # return True!
    if val == True:
        return val

main()
