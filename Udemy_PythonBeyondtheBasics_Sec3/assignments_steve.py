class MaxSizeList(object):


    def __init__(self, list_size):
        try:
            self.list_size = int(list_size)
            self.list_size = list_size
            self.list = []
        except ValueError as e:
            print('List size argument is wrong type: {}'.format(e.__str__()))
            # raise
        except Exception as e:
            print('Some other argument error: {}'.format(e.__str__()))
            # raise


    def push(self, string_item):
        try:
            assert string_item
            self.set_list(string_item)
            if len(self.list) > self.list_size:
                self.set_list()
        except Exception as e:
            print('The entered string is empty, or a problem occurred storing the string: {}'.format(e.__str__()))


    def get_list(self):
        return self.list

    def set_list(self, string_item=''):
        if string_item:
            self.list.append(string_item)
        else:
            self.list.pop(0)
