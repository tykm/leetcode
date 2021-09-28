class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

def reverse(node):
    prev = None
    while node:
        nxt = node.nextval
        node.nextval = prev
        prev = node
        node = nxt


a = Node('a')
b = Node('b')
c = Node('c')
a.nextval = b
b.nextval = c
reverse(a)
print(c.nextval.dataval)