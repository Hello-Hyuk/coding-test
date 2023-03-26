def shift_day(day_idx, change_day):
    if day_idx+change_day > 6:
        day_idx -= 7-change_day
    else : day_idx += change_day
    return day_idx

def solution(a, b):
    month_day = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    day_name = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    day_idx = 5
    answer = ''
    days = 0
    for i in range(1,a):
        days += month_day[i]
    change_day = (days+b) % 7
    day_idx = shift_day(day_idx, change_day-1)
    
    return day_name[day_idx]
    
    # 1월 14일
    # 14%7 6
    # 일 월 화 수 목 금 토 
    #               1 2
    # 3  4  5  6  7 8 9
    # 10 11 12 13 14 15 16
    # 17                23
    # 24                30
    # 31 
       #  1
    #  7  8
    #  14
    #  21 
    #  28
    #  28 1 2 3 4 5
    