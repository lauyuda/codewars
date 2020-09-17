import string
def encode_str(strng, shift):
    initial = ''
    code = string.ascii_lowercase + string.ascii_uppercase
    position_init =  0 
    for i in range(len(strng)):
        if strng[i] in code:
            position_init = strng.find(strng[i])
            position_code = code.find(strng[i])
            break
    initial = strng[position_init].lower() + code[(position_code + shift) % 52].lower()
    
    new = [initial[0], initial[1]]
    position = 0
    for i in range(len(strng)):
        if strng[i] in code:
            position = code.find(strng[i])
            new.append(code[(position + shift) % 52])
        else:
            new.append(strng[i])
    
    total_str = ''.join(new)
    length = len(new)
    length5 = length // 4
    length1 = 0
    while length1 < length5:
        length1 += 1
        length5 = length - length1 * 4
        
    
    length2 = length1 + length1
    length3 = length2 + length1
    length4 = length3 + length1
    message1 = total_str[0:length1]
    message2 = total_str[length1:length2]
    message3 = total_str[length2:length3]
    message4 = total_str[length3:length4]
    message5 = total_str[length4:]
    total_message = [message1, message2, message3, message4, message5]
    if message5 == '':
        total_message.remove('')
    '''
    print(message1)
    print(message2)
    print(message3)
    print(message4)
    print(message5)
    '''
    return total_message

def decode(arr):
    code = string.ascii_uppercase + string.ascii_lowercase
    print(arr)
    first = code.find(arr[0][0])
    second = code.find(arr[0][1])
    shift = second - first
    if arr[0][2:4] == 'h ':
        shift += 26
    strng = ''.join(arr)[2:]
    new = []
    print(strng)
    for i in range(len(strng)):
        if strng[i] in code:
            position = code.find(strng[i])
            new.append(code[(position - shift) % 52])
        else:
            new.append(strng[i])
    print(new)
    return ''.join(new)