def findMaxMin(number_list):
    upper_num = max(number_list)
    lower_num = min(number_list)
    all_list=[]
    
    
    if lower_num == upper_num: #if all numbers are same in  a list
        all_list = [upper_num]
    elif lower_num < upper_num:
        all_list = [lower_num, upper_num]
    else:
        return False
    return all_list
    
