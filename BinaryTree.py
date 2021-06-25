# Definition for a binary tree node.
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def isSymmetric(root):
    if not root:
        return True
    return areMirror(root.left,root.right)

def areMirror(leftroot,rightroot):
    if not leftroot or not rightroot:
        return(leftroot==rightroot)
    if leftroot.val != rightroot.val:
        return False
    return (areMirror(leftroot.left,rightroot.right) and areMirror(leftroot.right,rightroot.left));


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(isSymmetric(root))