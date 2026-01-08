# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root,res):
            if not root:
                return 0
            leftMax=dfs(root.left, res)
            rightMax=dfs(root.right, res)

            leftMax=max(leftMax,0)
            rightMax=max(rightMax,0)

            res[0]=max(res[0], root.val+leftMax+rightMax)
            return root.val+max(leftMax,rightMax)
        res=[root.val]
        dfs(root, res)
        return res[0]
