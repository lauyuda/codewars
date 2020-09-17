def domain_name(url):
    count = 0
    list = url.split('.')
    position = url.find('://www.')

    if 'www' in list[0]:
        return list[1]
    elif 'http' not in list[0]:
        return list[0]
    else:
        position = url.find('://') + 3
        return list[0][position:]
    pass