from Node import Node


class Singly_LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def length(self):
        if self.is_empty():
            return None

        current_node = self.head
        itr = 1
        while current_node is not None:
            current_node = current_node.next
            itr += 1

        return itr

    def insert_last(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            temp = self.tail
            temp.next = node
            self.tail = temp.next

    def insert_first(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            temp = self.head
            self.head = node
            self.head.next = temp

    def print(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def remove_first(self):
        temp = self.head.next
        self.head = None
        self.head = temp

    def remove_last(self):
        current_node = self.head
        while current_node.next.next is not None:
            current_node = current_node.next

        current_node.next = None
        self.tail = current_node

    def remove_at(self, pos):
        if self.is_empty():
            print("Empty list")
            return None

        if pos > self.length():
            print("Position out of range")
            return None

        prev_node = self.head
        itr = 0
        while itr + 1 is not pos - 1:
            prev_node = prev_node.next
            itr += 1

        current_node = self.head
        itr = 0
        while itr + 1 is not pos:
            current_node = current_node.next
            itr += 1

        prev_node.next = current_node.next
        current_node = None

    def insert_at(self, data, pos):
        if self.is_empty():
            print("Empty list")
            return None

        if pos > self.length():
            print("Position out of range")
            return None

        node = Node(data)
        if self.is_empty():
            self.head = node
            self.tail = node
            return None

        prev_node = self.head
        itr = 0
        while itr + 1 is not pos - 1:
            prev_node = prev_node.next
            itr += 1

        current_node = self.head
        itr = 0
        while itr + 1 is not pos:
            current_node = current_node.next
            itr += 1

        prev_node.next = node
        node.next = current_node
