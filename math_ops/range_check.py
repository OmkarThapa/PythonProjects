def range_check(n,lowest,highest):
    '''
    Function checks is it low or high from given range.
    This function accept 3 parameter to first is the number which we have to check and other two is the range.
    if the number not between two number return false. 
    
    '''
    if n in range(lowest,highest+1):
        print(f'{n} is between {lowest} and  {highest}')
    else:
        print(f'{n} is not in range')
        
        

        
