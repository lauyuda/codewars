import string
def phone(strng, num):
    alphanum = string.ascii_lowercase + string.ascii_uppercase + '1234567890'
    special = '!@#$%&*_;?'
    list = strng.split('\n')
    list.remove('')
    number = []
    name = []
    address = []
    to_add_num = ''
    to_add_name = ''
    to_add_add = ''
    plus_posit = 0
    angle1_posit = 0
    angle2_posit = 0
    add_posit = 0
    for data in list:
        plus_posit = data.find('+')
        if data[plus_posit + 2].isdigit():
            to_add_num = data[plus_posit + 1 : plus_posit + 1 + 15]
        else:
            to_add_num = data[plus_posit + 1 : plus_posit + 1 + 14]
        number.append(to_add_num)
        data = data.replace('+' + to_add_num, '')

        angle1_posit = data.find('<')
        angle2_posit = data.find('>')
        to_add_name = data[angle1_posit + 1 : angle2_posit]
        name.append(to_add_name)
        data = data.replace('<' + to_add_name + '>', '')
        
        temp = []
        for i in range(len(data)):
            if data[i].isalnum():
                add_posit = i
                break
        data = data[add_posit:].replace('_', ' ').replace(', ', ' ')
        for remove in special:
            data = data.replace(remove, '').strip()
        temp = data.split(' ')
        data = ' '.join(temp)
        address.append(data.replace('  ', ' '))
        print(data)
        
    mark = 0
    count = 0
    for i in number:
        if i == num:
            count += 1
    if count == 1:
        mark = number.index(num)
        return 'Phone => {}, Name => {}, Address => {}'.format(number[mark], name[mark], address[mark])
    elif count == 0:
        return 'Error => Not found: {}'.format(num)
    else:
        return 'Error => Too many people: {}'.format(num)
