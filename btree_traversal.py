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


def in_order(current, result):
    if not current:
        return
    in_order(current.left, result)
    result.append(current.key)
    in_order(current.right, result)
    return result


def pre_order(current):
    if not current:
        return
    print(current.key, end=' ')
    pre_order(current.left)
    pre_order(current.right)


def breadth_first_search(root):
    queue = [root]
    while queue:
        tmp_queue = []
        for element in queue:
            print(element.key, end=' ')
            if element.left:
                tmp_queue.append(element.left)
            if element.right:
                tmp_queue.append(element.right)
        queue = tmp_queue
        print()


def main():
    root = read_data()
    print(in_order(root, []))
    pre_order(root)
    print()
    print('-'*80)
    breadth_first_search(root)


main()
