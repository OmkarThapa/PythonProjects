def collatz_conjecture(n):
    '''
    This function returns list of the iterated number till 0.1 after that it repeats itself
    and display values 4.0,0.2 and 0.1 again and again.
       
    '''
    value_list=[n]
    #limit the length of list till 1000 values
    while len(value_list)<1000:
        # if n is even n=n\2
        if n%2==0:
            n/=2
            value_list.append(n)
        #if n is odd n = 3n+1
        else:
            n = (3*n)+1
            value_list.append(n)         
    return value_list

