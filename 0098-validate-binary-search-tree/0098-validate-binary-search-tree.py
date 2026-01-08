# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #DFS
        # def validbst(node,left, right):
        #     if not node:
        #         return True
        #     if not (left<node.val<right):
        #         return False
            
        #     return (validbst(node.left,left,node.val) and
        #     validbst(node.right,node.val,right))
        # return validbst(root, float("-infinity"),float("infinity"))

        #BFS
        if not root:
            return True

        q=deque()
        q.append((root, float("-infinity"),float("infinity") ))

        while q:
            node, left, right=q.popleft()
            if not (left < node.val < right):
                return False
            if node.left:
                q.append((node.left, left, node.val))
            if node.right:
                q.append((node.right, node.val, right))

        return True
                

            

        