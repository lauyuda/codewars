import string
def rot13(message):  
    alpha = string.ascii_lowercase + string.ascii_lowercase[:13] + string.ascii_uppercase + string.ascii_uppercase[:13]
    code = ''
    for i in range(len(message)):
        if message[i].isalpha():
            position = alpha.find(message[i])
            code += alpha[position + 13]
        else:
            code += message[i]
    return code