# Definition for a binary tree node.
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def sortedArrayToBST(nums):
    if nums is None:
        return None
    def check(nums,left,right):
        if left > right:
            return None
        mid = int((left+right)/2)
        obj = TreeNode(nums[mid])
        obj.left = check(nums,left,mid-1)
        obj.right = check(nums,mid+1,right)
        return obj
    return check(nums,0,len(nums)-1)


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(4)
# root.right.right = TreeNode(3)
root = [-10,-3,0,5,9]
print(sortedArrayToBST(root))