class Node:
    def __init__(self, data, next_element=None):
        self.data = data
        self.next_element = next_element


def hashing(string, m):
    p = 1000000007
    x = 263
    tmp_sum = sum([(ord(element) * x ** k) % p for k, element in enumerate(string)])
    return tmp_sum % p % m


def add(string, ht, m):
    h = hashing(string, m)
    cell = ht[h]
    node = Node(string)
    if not cell:
        ht[h] = node
    else:
        node.next_element = cell
        ht[h] = node


def find(string, ht, m):
    result = 'no'
    h = hashing(string, m)
    cell = ht[h]
    if not cell:
        return result
    while cell:
        if cell.data == string:
            result = 'yes'
            return result
        cell = cell.next_element
    return result


def main():
    m = int(input())
    ht = [None for _ in range(m)]
    n = int(input())
    for i in range(n):
        command, arg = input().split()
        if command == 'add':
            add(arg, ht, m)
        elif command == 'find':
            find(arg, ht, m)
        else:
            print('bad command')


main()
