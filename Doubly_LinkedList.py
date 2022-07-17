from Node import Node


class Doubly_LinkedList:
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

    def insert_first(self, data):
        node = Node(data)

        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def insert_last(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = self.tail.next

    def remove_first(self):
        if self.is_empty():
            print("Empty List")
            return None

        self.head = self.head.next
        self.head.prev = None

    def remove_last(self):
        if self.is_empty():
            print("Empty List")
            return None

        self.tail = self.tail.prev
        self.tail.next = None

    def insert_at(self, data, pos):
        if self.is_empty():
            print("Empty List")
            return None

        if pos > self.length():
            print("Position out of range")
            return None

        node = Node(data)
        if self.is_empty():
            self.head = node
            self.tail = node
            return None

        current_node = self.head
        itr = 0
        while itr + 1 is not pos:
            current_node = current_node.next
            itr += 1

        temp = current_node.prev
        node.next = current_node
        current_node.prev = node
        temp.next = node
        node.prev = temp

    def remove_at(self, pos):
        if self.is_empty():
            print("Empty list")
            return None

        if pos > self.length():
            print("Position out of range")
            return None

        current_node = self.head
        itr = 0
        while itr + 1 is not pos:
            current_node = current_node.next
            itr += 1

        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev
        # print(current_node.prev.data)
        current_node = None

    def print_descending(self):
        current_node = self.tail

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev

    def print_ascending(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next