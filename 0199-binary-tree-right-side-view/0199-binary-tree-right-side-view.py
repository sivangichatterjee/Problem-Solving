# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]

        q=deque()
        if root:
            q.append(root)

        while q:
            q_size=len(q)
            for i in range(len(q)):
                node=q.popleft()
                if i==q_size-1:
                    print(node.val)
                    ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return ans

        