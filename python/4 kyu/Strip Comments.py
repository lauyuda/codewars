def solution(string,markers):
    list = string.split('\n')
    mark_str = ''.join(markers)
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] in mark_str:
                position = j
                list[i] =  list[i][:j].strip()
                break
    answer = '\n'.join(list)
    return answer