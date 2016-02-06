class Node(object):
    def __init__(self, num):
        self.n = num
        self.left = None
        self.right = None

    def insert(self, num):
        if num > self.n:
            if self.right is None:
                self.right = Node(num)
            else:
                self.right.insert(num)
        else:
            if self.left is None:
                self.left = Node(num)
            else:
                self.left.insert(num)

    def find(self, num):
        if self.n == num:
            return True
        elif num > self.n and self.right is not None:
            print "Right"
            return self.right.find(num)
        elif self.left is not None:
            print "Left"
            return self.left.find(num)

        return False

    def find_min(self):
        if self.left is None:
            return self.n
        else:
            return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.n
        else:
            return self.right.find_max()

    def __str__(self):
        return str(self.n)


if __name__ == '__main__':
    root = Node(10)
    root.insert(15)
    root.insert(25)
    root.insert(4)
    root.insert(5)

    print root

    print root.find(5)

    print "Min value " + str(root.find_min())
    print "Max value " + str(root.find_max())
