class MyCalendar(object):
    def __init__(self):
        self.booking = []

    def book(self, start, end):
        for i, j in self.booking:
            if i < end and start < j:
                return False
        self.booking.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)