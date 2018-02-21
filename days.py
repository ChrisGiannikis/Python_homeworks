import datetime

cur_date = datetime.datetime.now()
date_str = cur_date.strftime("%A")
day_number = cur_date.strftime("%d")
def weekDay(year, month, day):
    offset = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
    week   = ['Sunday',
              'Monday',
              'Tuesday',
              'Wednesday',
              'Thursday',
              'Friday',
              'Saturday']
    afterFeb = 1
    if month > 2: afterFeb = 0
    aux = year - 1700 - afterFeb
    # dayOfWeek for 1700/1/1 = 5, Friday
    dayOfWeek  = 5
    # partial sum of days betweem current date and 1700/1/1
    dayOfWeek += (aux + afterFeb) * 365
    # leap year correction
    dayOfWeek += aux / 4 - aux / 100 + (aux + 100) / 400
    # sum monthly and day offsets
    dayOfWeek += offset[month - 1] + (day - 1)
    dayOfWeek %= 7
    return week[dayOfWeek]
s = 0
for k in range(2018,2029):
    for i in range(1,13):
        for j in range(1,32):
            if j == int(day_number) and weekDay(k, i, j) == date_str:
                s += 1
print "There will be another " , s , date_str , " for the next 10 years that will be the" , int(day_number) , "of each month"
