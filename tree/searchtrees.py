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
