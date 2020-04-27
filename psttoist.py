time = input("enter time in pst(hh:mm am/pm): ")
hours = int(time[0:2])
min = int(time[3:5])
if hours == 11 and min == 30 and time[-2].lower()=='a':
    print("12 midnight")
elif hours == 11 and min == 30 and time[-2].lower()=='p':
    print("12 noon")
elif hours>11 and min>=30 and time[-2].lower()=='a':
    hours+=12
    min+=30
    if min >= 60:
        min = min-60
        hours+=1
    if hours>12:
        hours-=12
    print('Same day\n', hours,':', min, 'PM')
elif hours<11 and min<=30 and time[-2].lower()=='a':
    hours+=12
    min+=30
    if min >= 60:
        min = min-60
        hours+=1
    if hours>12:
        hours-=12
    print('Same Day\n', hours,':', min, 'PM')
elif hours>11 and min>=30 and time[-2].lower()=='p':
    hours+=12
    min+=30
    if min >= 60:
        min = min-60
        hours+=1
    if hours>12:
        hours-=12
    print('Next Day\n', hours,':', min, 'AM')
elif hours<11 and min<=30 and time[-2].lower()=='p':
    hours+=12
    min+=30
    if min >= 60:
        min = min-60
        hours+=1
    if hours>12:
        hours-=12
    print('Next Day\n', hours,':', min, 'AM')
