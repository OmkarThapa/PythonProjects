def alpha_counter(str):
    '''
    This is function which get sentence as input and count every alphabets. Avoid space and special characters.
    output numbers
    Also, count cases of alphabets
    
    '''
    lowercounter= 0
    uppercounter=0
    
    for alpha in str:
        if alpha.isupper():
            uppercounter+=1
        elif alpha.islower():
            lowercounter+=1
        else:
            pass
    
    print(f'{uppercounter} is the count of upper case')
    print(f'{lowercounter} is the count of lower case')
    print(f'{uppercounter+lowercounter} is the alphabes')