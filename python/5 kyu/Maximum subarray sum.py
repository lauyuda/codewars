def max_sequence(arr):
    start = 0
    sum = 0
    list = []
    
    for i in range(len(arr)):
        if i == 0:
            start = 0
            sum = arr[0]
            list.append(sum)
            continue
        if sum + arr[i] > arr[i]:         
            sum += arr[i]
        else:
            start = i
            sum = arr[i]
        list.append(sum)
        
    if len(list) > 0 and max(list) > 0:
        return max(list)
    return 0