class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []

        # recursively get left subtree, current node, then right subtree
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
