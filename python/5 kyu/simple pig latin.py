def pig_it(text):
    string = text.split()
    translate = []
    
    for word in string:
        if word.isalnum():
            translate.append(word[1:] + word[0] + 'ay')
        else:
            translate.append(word[1:] + word[0])
  
    return ' '.join(translate)