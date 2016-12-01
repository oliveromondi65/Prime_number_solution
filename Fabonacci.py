def Fabonacci(arg): 
    for x in range (arg): #taking values from 0 to arg
    	if arg == 0:
    		return 0
    
    	elif arg == 1: 
    		return 1
    
    	else: 
    		return F(arg-1)+F(arg-2)