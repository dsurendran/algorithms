class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def find_path(node, path, key):
    if node is None:
        return
    path.append(node.key)
    if node.key == key:
        return True
    left = False
    right = False
    if node.left is not None:
        left = find_path(node.left, path, key)
    if node.right is not None:
        right = find_path(node.right, path, key)
    if left or right:
        return True

    path.pop()
    return False


def find_lca(root_node, key1, key2):
    path1 = []
    path2 = []
    if not find_path(root_node, path1, key1) or not find_path(root_node, path2, key2):
        return -1
    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break;
        i += 1
    return path1[i - 1]


def find_lca_1(root_node, key1, key2):
    if root_node is None:
        return None
    if root_node.key == key1 or root_node.key == key2:
        return root_node

    left_lca = find_lca_1(root_node.left, key1, key2)
    right_lca = find_lca_1(root_node.right, key1, key2)

    if left_lca and right_lca:
        return root_node

    return left_lca if left_lca is not None else right_lca


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print "LCA(4, 5) = %d" % (find_lca(root, 4, 5, ))
print "LCA(4, 6) = %d" % (find_lca(root, 4, 6))
print "LCA(3, 4) = %d" % (find_lca(root, 3, 4))
print "LCA(2, 4) = %d" % (find_lca(root, 2, 4))

print "LCA(2, 4) = ", find_lca_1(root, 2, 4).key


