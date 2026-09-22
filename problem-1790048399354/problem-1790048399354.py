# Last updated: 9/22/2026, 9:09:59 AM
1class MyCalendarThree:
2
3    def __init__(self):
4        self.events = {}
5
6    def book(self, startTime, endTime):
7        self.events[startTime] = self.events.get(startTime, 0) + 1
8        self.events[endTime] = self.events.get(endTime, 0) - 1
9
10        current = 0
11        maximum = 0
12
13        for time in sorted(self.events):
14            current += self.events[time]
15            maximum = max(maximum, current)
16
17        return maximum