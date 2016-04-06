class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def get_vertical_order(root, dist_from_root, m):
    if root is None:
        return
    try:
        m[dist_from_root].append(root.data)
    except:
        m[dist_from_root] = [root.data]
    get_vertical_order(root.left, dist_from_root - 1, m)
    get_vertical_order(root.right, dist_from_root + 1, m)


def print_vertical_order(root):
    m = dict()
    dist_from_root = 0
    get_vertical_order(root, dist_from_root, m)
    for index, value in enumerate(sorted(m)):
        for i in m[value]:
            print i,
        print


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)
print "Vertical order traversal is"

print_vertical_order(root)
