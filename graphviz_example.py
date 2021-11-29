import graphviz
import sys

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        left = self.left.key if self.left else None
        right = self.right.key if self.right else None
        return 'key: {}, left: {}, right: {}'.format(self.key, left, right)


def read_data():
    n = int(input())
    nodes = [Node(0) for _ in range(n)]
    for i in range(n):
        key, left, right = map(int, sys.stdin.readline().split())
        nodes[i].key = key
        if left != -1:
            nodes[i].left = nodes[left]
        if right != -1:
            nodes[i].right = nodes[right]
    return nodes[0]


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



def main():
    root = read_data()
    dot = graphviz.Digraph()
    breadth_first_search(root, dot)
    dot.render('g1.gv')


main()

