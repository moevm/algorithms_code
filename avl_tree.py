import graphviz
import sys

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 0 # высота считается в ребрах

    def __str__(self):
        left = self.left.key if self.left else None
        right = self.right.key if self.right else None
        return 'key: {}, left: {}, right: {}'.format(self.key, left, right)


def breadth_first_search(root, dot):
    queue = [root]
    dot.node(str(root.key))
    while queue:
        tmp_queue = []
        for element in queue:
            if element.left:
                dot.node(str(element.left.key))
                dot.edge(str(element.key), str(element.left.key))
                tmp_queue.append(element.left)
            if element.right:
                dot.node(str(element.right.key))
                dot.edge(str(element.key), str(element.right.key))
                tmp_queue.append(element.right)
        queue = tmp_queue

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self.root = self.insert_rec(key, self.root)

    def insert_rec(self, key, node):
        if not node:
            node = Node(key)

        elif key < node.key:
            node.left = self.insert_rec(key, node.left)
            # после добавления левого поддерева
        else:
            node.right = self.insert_rec(key, node.right)
            if self.get_height(node.right) - self.get_height(node.left) == 2:
                if key < node.right.key:
                    node = self.big_left_rotate(node)
                else:
                    node = self.small_left_rotate(node)
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
        return node

    def get_height(self, node):
        if not node:
            return -1
        else:
            return node.height

    def small_left_rotate(self, node_a):
        node_b = node_a.right
        Lb = node_b.left
        node_a.right = Lb
        node_b.left = node_a

        node_a.height = max(self.get_height(node_a.right), self.get_height(node_a.left)) + 1
        node_b.height = max(self.get_height(node_b.right), self.get_height(node_b.left)) + 1

        return node_b

    def big_left_rotate(self, node_a):
        pass


def main():
    nodes = list(map(int, input().split()))
    avl_tree = AVLTree()
    for index, node in enumerate(nodes):
        dot = graphviz.Digraph()
        avl_tree.insert(node)
        breadth_first_search(avl_tree.root, dot)
        dot.render('g{}.gv'.format(index))


main()
