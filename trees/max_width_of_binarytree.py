# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        max_width=0
        queue=deque([(root,0)])
        while queue:
            n=len(queue)
            # Use queue[0][1] and queue[-1][1] to get only the index.
            first_ind=queue[0][1]
            last_ind=queue[-1][1]
            for _ in range(n):
                node,index=queue.popleft()
                norm_ind = index-first_ind
                if node.left:
                    queue.append((node.left,2*norm_ind))
                if node.right:
                    queue.append((node.right,2*norm_ind+1))
            max_width= max(max_width,last_ind-first_ind+1)
        return max_width