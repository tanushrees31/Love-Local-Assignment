class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: int, q: int) -> int:
        
        if p > q:
            p, q = q, p

        while root:
            
            if root.val > q:
                root = root.left
            
            elif root.val < p:
                root = root.right
            
            else:
                return root.val

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)


solution = Solution()


result = solution.lowestCommonAncestor(root, 2, 8)
print("The LCA of nodes 2 and 8 is",result) 
