def valid_parentheses(string):
    sum = 0
    for i in string:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        
        if sum < 0:
            return False
    
    if sum == 0:
        return True
    else:
        return False
