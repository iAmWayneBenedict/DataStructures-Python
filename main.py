from Singly_LinkedList import Singly_LinkedList

new_node = Singly_LinkedList()
new_node.insert_first(1)
new_node.insert_last(2)
new_node.insert_last(3)
new_node.insert_last(4)
new_node.insert_last(5)
new_node.insert_last(6)

# print(new_node.head.data)
new_node.remove_first()
new_node.remove_last()
new_node.remove_at(3)
new_node.insert_at(4, 3)
new_node.print()
# print(new_node.length())
