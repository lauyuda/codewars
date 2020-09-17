def order_weight(strng):
    print(strng)
    weight_list = strng.split()
    weight_list.sort()
    sum_list = []
    entries = len(weight_list)
    
    for i in weight_list:
        sum_list.append(weight(i))
            
    for i in range(entries):
        for j in range(entries - 1 - i):
            if sum_list[j] > sum_list[j + 1]:
                weight_list[j], weight_list[j + 1] = weight_list[j + 1], weight_list[j]
                sum_list[j], sum_list[j + 1] = sum_list[j + 1], sum_list[j]
    weight_str = ' '.join(weight_list)
    
    return weight_str

def weight(weight):
    sum = 0
    for i in range(len(weight)):
        sum += int(weight[i])
    return sum