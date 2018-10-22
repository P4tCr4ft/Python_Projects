class MaxSizeList(object):

    def __init__(self, list_size):
        try:
            self.list_size = int(list_size)
        except ValueError as e:
            print('Size argument is wrong type'.format(e.__str__()))
            # raise
        except Exception as e:
            print('Some other argument error: {}'.format(e.__str__()))
            # raise
        self.list_size = list_size
        self.list = []

    def push(self, string_item):
        self.list.append(string_item)
        if len(self.list) > self.list_size:
            self.list.pop(0)

    def get_list(self):
        return self.list
