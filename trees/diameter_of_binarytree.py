class Solution(object):
    def diameterOfBinaryTree(self, root):
        res = [0]
        def maxdiam(node):
            if not node :
                return 0
            left_height =  maxdiam(node.left)
            right_height = maxdiam(node.right)
            diam = left_height + right_height
            res[0] = max(res[0] , diam)
            return 1 + max(left_height , right_height)
        maxdiam(root)
        return res[0]