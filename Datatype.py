def data_type(arg):
  if arg is None: #testing for none
		return 'no value'
  
  
  elif type(arg) == str: #testing for strings
    length = len(arg)
    return length
  
  
  
  elif type(arg) == bool: #testing for boolean
    return arg
  
  elif type(arg) == int: #testing for integer
    if arg<100:
      return 'less than 100'
    elif arg==100:
      return 'equal to 100'
    elif arg>100:
      return 'more than 100'
  
  elif type(arg) == list: #testing for lists
    if len(arg) > 2:
      third_term = arg[2]
      return third_term
    
    elif len(arg) < 2 or len(arg) ==2:
      return None