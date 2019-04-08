hourTime = input("Please enter the time in hour AM/PM format e.g. 07:45:00 PM ")
timeCheck = hourTime.split(' ', 2)
times = timeCheck[0]
merid = timeCheck[1]
hourCheck = hourTime.split(':', 3)
hour = hourCheck[0]
mins = hourCheck[1]
secsTime = hourCheck[2]
secssplit = secsTime.split(" ", 2)
secs = secssplit[0]
def timeConversion(merid, hour, mins, secs):
    if merid == "AM" or merid == "PM":
        if merid == 'AM':
            if  hour == '12':
                milTime = "00" + ":" + mins + ":" + secs
            else:
                milTime = hour + ":" + mins + ":" + secs
        elif hour == '12':
            milTime = hour + ":" + mins + ":" + secs
        else:
            newHour = int(hour) + 12
            milTime = str(newHour) + ":" + mins + ":" + secs 
        return milTime
    else:
        return "Your time format is wrong, Please check it and try again"

timeValue = str(timeConversion(merid, hour, mins, secs))

print("The military time format is "+ str(timeValue))

#Method 1
#using string splitting to determine if te time is am/pm