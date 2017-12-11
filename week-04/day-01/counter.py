class Counter(object):
    def __init__(self, count_base = 0):
        self.count_base = count_base

    def add(self, number = 1):
        self.count_base += number

    def get(self):
        return self.count_base

    def reset(self):
        self.count_base = 0