class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(left,right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val==right.val and dfs(left.left,right.right)and dfs(left.right,right.left))
        return dfs(root.left,root.right)