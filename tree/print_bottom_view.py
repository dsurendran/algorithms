class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


def get_vertical_distance(node, distance, m):
    if not node:
        return
    m[distance] = node.data
    get_vertical_distance(node.left, distance - 1, m)
    get_vertical_distance(node.right, distance + 1, m)


def print_bottom_view(node):
    m = dict()
    distance = 0
    get_vertical_distance(node, distance, m)
    for index, key in enumerate(sorted(m)):
        print m[key], " "


print_top_view(root)
