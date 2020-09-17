def move_zeros(array):
    count = len([x for x in array if x == 0 and x is not False])
    
    list = [x for x in array if x != 0 or x is False]

    while count > 0:
        list.append(0)
        count -= 1
    return list
