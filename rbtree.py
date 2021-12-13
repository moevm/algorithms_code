import graphviz

BLACK = 'black'
RED = 'red'


class Node:
    def __init__(self, key, color, parent=None):
        self.key = key
        self.left = None
        self.right = None
        self.color = color
        self.parent = parent

    def __str__(self):
        left = self.left.key if self.left else None
        right = self.right.key if self.right else None
        parent = self.parent.key if self.parent else None
        return 'key: {}, left: {}, right: {}, color: {}, parent: {}'.format(self.key, left, right, self.color, parent)


def breadth_first_search(root, dot):
    queue = [root]
    dot.node(str(root.key), color=root.color)
    while queue:
        tmp_queue = []
        for element in queue:
            if element.left:
                dot.node(str(element.left.key), color=element.left.color)
                dot.edge(str(element.key), str(element.left.key))
                tmp_queue.append(element.left)
            if element.right:
                dot.node(str(element.right.key), color=element.right.color)
                dot.edge(str(element.key), str(element.right.key))
                tmp_queue.append(element.right)
        queue = tmp_queue


class RBTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key, BLACK)
        else:
            current = self.root
            while current:
                if key < current.key:
                    if not current.left:
                        new_node = Node(key, RED, parent=current)
                        current.left = new_node
                        break
                    current = current.left
                else:
                    if not current.right:
                        new_node = Node(key, RED, parent=current)
                        current.right = new_node
                        break
                    current = current.right
            self.fix_tree(new_node)

    def fix_tree(self, node):
        while node.parent and node.parent.color == RED:
            grandparent = node.parent.parent
            if node.parent == grandparent.left:
                uncle = grandparent.right

                if not uncle or uncle.color == BLACK: # дядя отсутствует или черный
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    self.right_rotate(grandparent)
                    node.parent.color = BLACK
                    grandparent.color = RED

                else: # дядя красный
                    uncle.color = BLACK
                    node.parent.color = BLACK
                    grandparent.color = RED

            else: # если родитель нового узла правый сын
                pass
        if self.root.color == RED:
            self.root.color = BLACK

    def left_rotate(self, node): # node - отец нового элемента
        new_node = node.right
        parent = node.parent

        node.right = new_node.left # Lb
        if node.right:
            node.right.parent = node

        new_node.left = node
        node.parent = new_node

        if not parent:
            self.root = new_node

        else:
            if parent.left == node:
                parent.left = new_node
            else:
                parent.right = new_node

    def right_rotate(self, node):
        new_node = node.left
        parent = node.parent

        node.left = new_node.right
        if node.left:
            node.left.parent = node

        new_node.right = node
        node.parent = new_node

        if not parent:
            self.root = new_node

        else:
            if parent.left == node:
                parent.left = new_node
            else:
                parent.right = new_node


def main():
    nodes = list(map(int, input().split()))
    rb_tree = RBTree()
    for index, node in enumerate(nodes):
        dot = graphviz.Digraph()
        rb_tree.insert(node)
        breadth_first_search(rb_tree.root, dot)
        dot.render('g{}.gv'.format(index))


main()
