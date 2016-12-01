#function that tests for prime numbers
def prime_number_solution(number):
	for x in range(number):
    		if number % x == 0:
        		return False
    	return True


