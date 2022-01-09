def alpha_counter(str):
    '''
    This is function which get sentence as input and count every alphabets. Avoid space and special characters.
    output numbers
    Also, count cases of alphabets
    
    '''
    d={'upper':0 , 'lower':0}
    
    for alpha in str:
        if alpha.isupper():
            d['upper']+=1
        elif alpha.islower():
            d['lower']+=1
        else:
            pass
    
    print(f'{d["upper"]} is the count of upper case')
    print(f'{d["lower"]} is the count of lower case')
    print(f'{d["upper"]+d["lower"]} is the alphabes')