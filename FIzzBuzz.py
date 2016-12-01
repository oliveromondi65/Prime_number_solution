#finction fizz_buzz that takes in argument arg
def fizz_buzz(arg):
  if arg%15==0: #testing for divisibility  by both 3 and 5 
	  return 'FizzBuzz'

  elif arg%3==0: #testing for divisibility by 3
	  return 'Fizz'

  elif arg%5==0: #testing for divisibility by 5
	  return 'Buzz'
    
  else: #return the number if not divisible by 3, 5 or both
	  return arg 