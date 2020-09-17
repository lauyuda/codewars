def rgb(r, g, b):

    if r < 0:
        r = 0
    elif r > 255:
        r = 255
    if g < 0:
        g = 0
    elif g > 255:
        g = 255
    if b < 0:
        b = 0
    elif b > 255:
        b = 255
  
    hex_r = hex(r)[-2].replace('x', '0') + hex(r)[-1]
    print(hex_r)
       
    hex_g = hex(g)[-2].replace('x', '0') + hex(g)[-1]
    print(hex_g)
    
    hex_b = hex(b)[-2].replace('x', '0') + hex(b)[-1]
    print(hex_b)
    
    return hex_r.upper() + hex_g.upper() + hex_b.upper()