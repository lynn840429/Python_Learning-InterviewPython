# =====================================
# FileName: binary_tree.py
# Usage: $python3 binary_tree.py
# Description: Generate a tree and traverse it.
# Dependency: x
# Author: Lynn <lynn840429@gmail.com>
# Version: v1.1.0
# =====================================
""" Import Packages """
# import os

""" User Defined Parameters """
# PARAMETER_1 = 1

""" Folder/Path/Parameters Setting """
# FOLDER_1 = "./"
# PATH_1 = "./"
# GLONAL_CONSTANT_NAME = 1

""" Class """
class Node(object):
    """
	Create Nodes: Root, Left child, Right child
	"""
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right



""" Function """
def traverse_deep(node=Node(0, 0, 0)):
    """
    Traverse Deep Function 1
    """
    if (node.data!=None):
        print(node.data)    # pre_travelsal
        if (node.left!=None):
            traverse_deep(node.left)
        #print(node.data)   # mid_travelsal
        if (node.right!=None):
            traverse_deep(node.right)
        #print(node.data)   # post_trvelsal
    else:
        print("Empty list")


def deep(root):
    """
    Traverse Deep Function 2
    """
    if not root:
        return
    print(root.data)    # pre_travelsal
    deep(root.left)
    # print(root.data)    # mid_travelsal
    deep(root.right)
    # print(root.data)    # post_trvelsal


def traverse_level(node=Node(0, 0, 0)):
    """
    Traverse Level Function 1
    """
    def insert(lineup):
        if not lineup:
            return

        root = lineup.pop(0)
        print(root.data)

        if (root.left!=None):
            lineup.append(root.left)
        if (root.right!=None):
            lineup.append(root.right)

        insert(lineup)
        
    if (node.data!=None):
        lineup = [node, ]
        insert(lineup)
    else:
        print("Empty list")


def lookup(root):
    """
    Traverse Level Function 2
    """
    row = [root]
    while row:
        #print(row)
        for n in row:
            print(n.data)
        
        row = [kid for item in row for kid in (item.left, item.right) if kid]


def maxDepth(root):
    """
    Calculate Max Depth
    """
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1


def isSameTree(p, q):
    """
    Check Two Trees are same or not
    """
    if p == None and q == None:
        return True
    elif p and q :
        return p.data == q.data and isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
    else :
        return False



""" Main """
def main():
    ### Generate Linked List
    tree = Node(1, Node(3, Node(7, Node(0)), Node(6)), Node(2, Node(5), Node(4)))

    ### Traverse Deep Function 1
    print("Traverse Deep:")
    traverse_deep(tree)

    ### Traverse Deep Function 2
    print("\nDeep:")
    deep(tree)

    ### Traverse Level Function 1
    print("\nTraverse Level:")
    traverse_level(tree)

    ### Traverse Level Function 2
    print("\nLookup:")
    lookup(tree)

    ### Calculate Max Depth
    print("\nDepth:")
    print(maxDepth(tree))

    ### Check Two Trees are same or not
    print("\nSame or not:")
    print(isSameTree(tree, tree))


""" Boilerplate Code"""
if __name__ == '__main__':
	main()
