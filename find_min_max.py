def find_min(lst):
    min_num = None
    for item in lst:
        if min_num == None or item < min_num:
            min_num = item
    return min_num
	
def find_max(lst):
    max_num = None
    for item in lst:
        if max_num == None or item > max_num:
            max_num = item
    return max_num
    
l = [-1, 2, 3, 6, 9, -2, 4, 5, -3]
print(find_min(l))   
print(find_max(l))   