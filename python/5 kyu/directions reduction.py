def dirReduc(arr):
    print(arr)
    reducible = True
    count = 0
    i = 0
    
    while reducible:
        count = 0
        direction = []
        #print('reduce')
        print('arr is ', arr)
        print('length:', len(arr))
        while i <= len(arr):
            #print(arr[i])
            print('i is ', i)
            #print(direction)
            if i == len(arr) - 1:
                direction.append(arr[i])
                arr = direction
                print(direction)
                i = 0
                print('break here')
                break
            elif i == len(arr):
                arr = direction
                i = 0
                break
            if i < len(arr):
                if arr[i] == 'NORTH' and arr[i + 1] == 'SOUTH':
                    count += 1
                    i += 2
                    print('ok')
                    continue
                elif arr[i] == 'SOUTH' and arr[i + 1] == 'NORTH':
                    i += 2
                    count += 1
                    continue
                elif arr[i] == 'EAST' and arr[i + 1] == 'WEST':
                    i += 2
                    count += 1
                    continue
                elif arr[i] == 'WEST' and arr[i + 1] == 'EAST':
                    i += 2
                    count += 1
                    continue
                else:
                    direction.append(arr[i])
                    print('dir is ', direction)
                    #i = 0
                    print('appended ', arr[i])
  
            i += 1
        if count == 0:
            print('break count')
            break
        
    print(direction)
    return direction