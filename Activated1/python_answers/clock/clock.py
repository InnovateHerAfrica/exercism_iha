class Clock(object):
    def __init__(self, h, m):
        self.m = (h*60 + m) % 1440
        if self.m < 0:
            self.m +=1440

    def add(self, m):
        self.m += m
        self.m = self.m % 1440
        if self.m < 0:
            self.m +=1440
        return self
    def __eq__(self, other):
                 return self.m == other.m
    def __repr__(self):
        return "%02d:%02d" % (self.m/60, self.m%60)
