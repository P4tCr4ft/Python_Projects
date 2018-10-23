# coding=utf-8

class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = val
        InstanceCounter.count += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    @classmethod
    def get_count(cls):
        return cls.count


class InstanceCounter2(object):
    count = 0

    def __init__(self, val):
        self.val = self.filterint(val)
        InstanceCounter2.count += 1

    @staticmethod
    def filterint(value):
        if not isinstance(value, int):
            return 0
        else:
            return value

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    @classmethod
    def get_count(cls):
        return cls.count