def sum_of_intervals(intervals):
    list = []
    for i in intervals:
        for value in range(i[0], i[1]):
            if value not in list:
                list.append(value)
    return len(list)