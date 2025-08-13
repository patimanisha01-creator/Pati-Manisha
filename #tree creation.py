#tree creation 
class Node:
    def __init__(self,val):
        self.left=None
        self.data=val
        self.right=None
root=Node(1)
root.left=Node(3)
root.right=Node(4)
root.right.left=Node(16)
root.left.right=Node(5)
root.left.right.left=Node(7)
#traversal
'''def Inorder(root):
    if(root==None):
        return
    Inorder(root.left)
    print(root.data)
    Inorder(root.right)
Inorder(root)'''
'''def preorder(root):
    if(root==None):
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)
preorder(root)'''
def postorder(root):
    if(root==None):
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data)
postorder(root)