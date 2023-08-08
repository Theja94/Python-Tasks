"""Create a class 'Time' and initialize it with hours and minutes.
Create a method addTime() which should take two Time objects
and add them.

E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
Create another method displayTime() which should print the time.
Also, create a method displayMinute() which should display the
total minutes in the Time.
E.g.- (1 hr 2 min) should display 62 minutes.
"""

class Time():

    def __init__(self, hours, mins):
        self.hours = hours
        self.mins = mins

    def addTime(t1, t2):
        t3 = Time(0,0)
        if t1.mins+t2.mins > 60:
            t3.hours = int((t1.mins+t2.mins)/60)
        t3.hours = t3.hours+t1.hours+t2.hours
        if t1.mins+t2.mins < 60:
            t3.mins = (t1.mins+t2.mins) 
        elif t1.mins+t2.mins > 120:
            t3.mins = (t1.mins+t2.mins)-120
        else:
            t3.mins = (t1.mins+t2.mins)-60

        return t3

    def displayTime(self):
        print(f"Time is {round(self.hours,3)} hour and {self.mins} minutes ")

    def displayMinute(self):
        print(round((self.hours*60)+self.mins,3))

a = Time(2,50)
b = Time(1,80)
c = Time.addTime(a,b)
c.displayTime()
c.displayMinute()
