from datetime import datetime
from datetime import date
from datetime import timedelta

# print(datetime.today())

today = datetime.today()
print(today)
print(type(today))

print("---------")

todaydate = date.today()

print(type(todaydate))
print(todaydate)

print("---------")

print(todaydate.month)
print(todaydate.day)
print(todaydate.year)

print("---------")

christmas = date(2018, 12, 25)

print(christmas)
print(type(christmas))

print(christmas - todaydate)
print((christmas - todaydate).days)

print("---------")

if christmas is not todaydate:
    print("Sorry there are still " + str((christmas - todaydate).days) + " days until Christmas!")
else:
    print("Yay it's Christmas!")

print("---------")

t = timedelta(days=4, hours=10)

print(type(t))
print(t.days)
print(t.seconds)

print("---------")

eta = timedelta(hours=23)

print(eta)
print(today)
print(today+eta)


