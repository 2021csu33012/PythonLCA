#python implementation inspired by geeksforgeeks.com

class Node:
    
    def __init__(self, key):
        self, key = key
        self.left = None
        self.right = None


    def fLCA(root, node1, node2):
        if root is None:
            return None

        if root.key == node1 or root.key == node2:
            return root

        leftLCA = fLCA(root.left, node1, node2)
        rightLCA = fLCA(root.right, node1, node2)

        if leftLCA is not None and rightLCA is not None:
            return root

        return rightLCA if rightLCA is not None else leftLCA


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
input1 = input("Enter first node: ")
print(input1)
input2 = input("Enter second node: ")
print(input2)
output = fLCA
print("result is: " + output + "")