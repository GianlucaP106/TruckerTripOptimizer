from datetime import datetime

def SecondsBetween(d1, d2):
    d1 = datetime.fromisoformat(d1)
    d2 = datetime.fromisoformat(d2)
    return int(abs((d1 - d2).total_seconds()))

day1 = "2022-03-02T19:00:00.000Z"
day1 = day1[0:10] + " " + day1[11:19]

day2 = "2022-03-04T12:00:00.000Z"
day2 = day2[0:10] + " " + day2[11:19]



print(SecondsBetween(day1,day2))