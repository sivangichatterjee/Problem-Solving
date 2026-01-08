# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #DFS
        # self.res=root.val
        # self.c=k
        # def dfs(node):
        #     if not node:
        #         return 0
            
        #     dfs(node.left)
        #     self.c-=1
        #     if self.c==0:
        #         self.res=node.val
        #         return
        #     dfs(node.right)

        # dfs(root)
        # return self.res

        #BFS
        curr=root
        stack=[]

        while curr or stack:
            while curr:
                stack.append(curr)
                curr=curr.left

            curr=stack.pop()
            k-=1
            if k==0:
                return curr.val
            curr=curr.right



            