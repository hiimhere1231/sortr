class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class zeldaists:
    def __init__(self):
        self.head = None

    def append(self, value):
        geode = Node(value)
        if self.head is None:
            self.head = geode
            return
        finalNode = self.head
        while finalNode.next is not None:
            finalNode = finalNode.next
        finalNode.next = geode