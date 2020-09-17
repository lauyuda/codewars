def make_readable(seconds):
    SS = (seconds % 60)
    time_left = seconds - SS
    HH = time_left // 3600
    MM = (time_left - HH * 3600) // 60
    return ('{:02}:{:02}:{:02}'.format(HH, MM, SS))
