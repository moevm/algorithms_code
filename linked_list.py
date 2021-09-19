class Node:
    def __init__(self, data, next_element=None):
        self.data = data
        self.next_element = next_element

    def __str__(self):
        next_element = None
        if self.next_element:
            next_element = self.next_element.data
        return 'data: {}, next_element: {}\n'.format(self.data, next_element)

class LinkedList:
    def __init__(self, root, tail):
        self.root = root
        self.tail = tail
        self.root.next_element = tail
        self.length = 2

    def __len__(self):
        return self.length

    def find(self, data):
        current = self.root
        while current:
            if current.data == data:
                return current
            current = current.next_element
        return 'not found\n'

    def append(self, root_element, element):
        if root_element.next_element:
            next_element = root_element.next_element
            root_element.next_element = element
            element.next_element = next_element
        else:
            root_element.next_element = element
            self.tail = element
        self.length += 1


root = Node('A')
tail = Node('z')
linked_list = LinkedList(root, tail)
print(linked_list.root, linked_list.tail)
print(len(linked_list))
print('-'*80)
new_node = Node('t')
linked_list.append(root, new_node)
new_node = Node('Q')
linked_list.append(tail, new_node)
print('try to find t:', linked_list.find('t'), 'try to find Q:', linked_list.find('Q'))
print(len(linked_list))
