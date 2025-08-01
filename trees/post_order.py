class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root :
            return[]
        return self.postorderTraversal(root.left)+self.postorderTraversal(root.right) + [root.val]