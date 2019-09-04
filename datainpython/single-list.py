class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linklist:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        cur = self.head

        if self.head:
            while cur.next:
                cur = cur.next
            cur.next = new_element
        else:
            self.head = new_element


    def is_empty(self):
        return bool(self.head)

    def insert(self, pos, new_element):
        if pos < 0 or pos > self.get_length():
            raise IndexError("insert插入时候，index 超过范围了")

        if pos == 0:
            new_element.next = self.head
            self.head = new_element

        tmp = self.head
        i = 0
        while i< pos:
            pre = tmp
            tmp = tmp.next
            i+=1

        new_element.next=pre.next
        pre.next = new_element

    def remove(self, pos):
        if pos < 0 or pos > self.get_length():
            raise IndexError("insert插入时候，index 超过范围了")

        i = 0
        tmp = self.head
        if pos ==0:
            self.head = tmp.next
            tmp.next = None
            return

        while i<pos:
            pre = tmp
            tmp =tmp.next
            i+=1

        pre.next = tmp.next
        tmp.next = None

    def get_length(self):
        i = 0
        tmp = self.head
        while tmp!=None:
            i += 1
            tmp = tmp.next
        return i