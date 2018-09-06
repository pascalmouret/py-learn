class List():
    tail = None

    def __init__(self, value):
        self.value = value

    def append(self, item):
        if not isinstance(item, List):
            item = List(item)
        
        if self.tail is None:
            self.tail = item
        else:
            self.tail.append(item)
