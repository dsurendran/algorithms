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

print "Vertical order traversal is"


def get_vertical_distance(node, distance, m):
    if not node:
        return
    if distance not in m:
        m[distance] = node.data
    get_vertical_distance(node.left, distance - 1, m)
    get_vertical_distance(node.right, distance + 1, m)


def print_top_view(root):
    m = dict()
    distance = 0
    get_vertical_distance(root, distance, m)
    for index, value in enumerate(sorted(m)):
        print m[value]

print_top_view(root)
