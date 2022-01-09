def unique_list(num):
    '''
    This function print list of unique number and sort out duplicates.
    Note: Unsorted  
    
    '''
    list_of_num =[]
    for n1 in num:
        if n1 not in list_of_num:
            list_of_num.append(n1)
    return list_of_num