import fractions
def mixed_fraction(s):
    number = s.split('/')
    positive = True
    if int(number[0]) // int(number[1]) < 0:
        positive = False
    whole = int(number[0]) // int(number[1])
    numerator = abs(int(number[0]))
    denominator = abs(int(number[1]))
    whole = (numerator // denominator)
    while numerator >= denominator:
        numerator -= denominator
    fraction = fractions.Fraction(int(numerator),int(denominator))
    
    string = ''
    if fraction > 0:
        string += str(fraction)
    
    if whole > 0 and fraction > 0:
        string = str(whole) + ' ' + string
    elif whole > 0:   
        string = str(whole) + string
    elif whole == 0 and fraction == 0:
        string = '0'
    
    if not positive:
        string = '-' + string

    return string