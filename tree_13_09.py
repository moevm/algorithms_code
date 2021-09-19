class Node:
    def __init__(self, data):
        self.data = data
        self.elements = []

    def __str__(self):
        next_elements = []
        if self.elements:
            for element in self.elements:
                next_elements.append(element.data)
        return 'data: {}, next_element: {}\n'.format(self.data, next_elements)

    def append_children(self, children):
        self.elements.extend(children)


class Tree:
    def __init__(self, root):
        self.root = root

    def print_tree(self, element):
        print(element)
        for child in element.elements:
            self.print_tree(child)


root = Node('A')
arr_nodes = [Node(chr(i)) for i in range(66, 70)]
root.append_children(arr_nodes)

arr_nodes_1 = [Node(chr(i)) for i in range(70, 72)]
arr_nodes[1].append_children(arr_nodes_1)

tree = Tree(root)
tree.print_tree(root)
