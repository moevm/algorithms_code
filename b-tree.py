import graphviz


class Node:
    def __init__(self, leaf):
        self.keys = []
        self.children = []
        self.leaf = leaf  # лист?

    def __str__(self):
        return ', '.join(map(str, self.keys)) if self.keys else 'None'


def breadth_first_search(root, dot):
    queue = [root]
    dot.node(str(root), shape='box')
    while queue:
        tmp_queue = []
        for element in queue:
            for child in element.children:
                dot.node(str(child), shape='box')
                dot.edge(str(element), str(child))
                tmp_queue.append(child)
        queue = tmp_queue


class BTree:
    def __init__(self, t):
        self.root = Node(True)
        self.t = t

    def insert(self, key):
        root = self.root
        if not len(root.keys): # пустое дерево
            self.root.keys.append(key)

        elif len(root.keys) == 2 * self.t - 1:  # количество ключей максимально возможно, превентивно разбиваем узел

            new_node = Node(False)
            self.root = new_node
            new_node.children.append(root)
            self.split_child(new_node, 0)
            self.insert_non_full(new_node, key)

        else:
            self.insert_non_full(root, key)

    def split_child(self, node, index):  # node - узел, ребенка которого будут делить, index - куда отправится узел посередине
        left_half = node.children[index]
        right_half = Node(left_half.leaf)

        node.keys.insert(index, left_half.keys[self.t-1]) # добавляем узел посередине

        right_half.keys = left_half.keys[self.t:]
        left_half.keys = left_half.keys[:self.t-1]

        if not left_half.leaf:
            right_half.children = left_half.children[self.t:]
            left_half.children = left_half.children[:self.t]

        node.children.insert(index+1, right_half) # сразу после i-го (левого) ребенка


    def insert_non_full(self, node, key): # элемент всегда добавляется в лист
        i = len(node.keys) - 1

        if node.leaf:

            while i >= 0 and key < node.keys[i]: # поиск места для вставки элемента
                i -= 1
            node.keys.insert(i+1, key)

        else:
            while i >= 0 and key < node.keys[i]: # поиск индекса нужного ребенка
                i -= 1
            i += 1

            if len(node.children[i].keys) == 2 * self.t - 1:  # количество ключей максимально возможно, превентивно разбиваем узел

                self.split_child(node, i)

                if key > node.keys[i]: # идем ли мы в правую часть детей после сплита
                    i += 1
            self.insert_non_full(node.children[i], key)


def main():
    nodes = list(map(int, input().split()))
    b_tree = BTree(3)
    for index, node in enumerate(nodes):
        dot = graphviz.Digraph()
        b_tree.insert(node)
        breadth_first_search(b_tree.root, dot)
        dot.render('g{}.gv'.format(chr(index + 65)))


main()
