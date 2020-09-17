def sum_pairs(ints, s):
    remainder = None
    seen_num = {}
    
    for i in range(len(ints)):
        remainder = s - ints[i]
        if remainder in seen_num:
            return [remainder, ints[i]]
        seen_num[ints[i]] = True
    
    return None