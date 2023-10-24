import datetime as d
#for todays date
print(d.datetime.now())
#for getting each value of day and time
print(d.date.today().strftime("%A"))
print(d.date.today().strftime("%a"))
print(d.date.today().strftime("%w"))
print(d.date.today().strftime("%W"))
print(d.date.today().strftime("%B"))
print(d.date.today().strftime("%b"))
print(d.date.today().strftime("%d"))
print(d.date.today().strftime("%D"))
