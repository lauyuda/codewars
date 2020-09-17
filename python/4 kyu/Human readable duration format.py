def format_duration(seconds):
    if seconds == 0:
        return 'now'
    
    ss = seconds % 60
    mm = seconds // 60 % 60
    hh = seconds // 3600 % 24
    dd = seconds // 86400 % 365
    yy = seconds // 31536000
    print(seconds)
    print(dd)
    
    sec = str(ss) + ' second'
    if ss > 1:
        sec += 's'
    min = str(mm) + ' minute'
    if mm > 1:
        min += 's'
    hr = str(hh) + ' hour'
    if hh > 1:
        hr += 's'
    day = str(dd) + ' day'
    if dd > 1:
        day += 's'
    yr = str(yy) + ' year'
    if yy > 1:
        yr += 's'
        
    time_list = [ss, mm, hh, dd, yy]
    print_list = [sec, min, hr, day, yr]
    string = ''
    count = 0
        
    for i in range(len(time_list)):
        if time_list[i] > 0:
            if count == 0:
                string = print_list[i]
                count += 1
            elif count == 1:
                string = print_list[i] + ' and ' + string
                count += 1
            elif count == 2:
                string = print_list[i] + ', ' + string
                count += 1
            elif count == 3:
                string = print_list[i] + ', ' + string
                count += 1
            elif count == 4:
                string = print_list[i] + ', ' + string
                count += 1
    print (string)
    return string