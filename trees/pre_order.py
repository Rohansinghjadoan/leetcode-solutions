class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return[]
        return[root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right)