#function that tests for prime numbers
def prime_number_solution(number): #function takes in number as an arguement
	for x in range(number):
    		if number % x == 0: #testing for prime numbers
        		return False
    	return True


