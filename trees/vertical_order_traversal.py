from collections import defaultdict,deque 
class Solution(object):
    def verticalTraversal(self, root):
        if not root:
            return []
        
        column_table = defaultdict(list)
        queue = deque([(root, 0, 0)])
        
        while queue:
            node, row, col = queue.popleft()
            column_table[col].append((row, node.val))
            if node.left:
                queue.append((node.left, row + 1, col - 1))
            if node.right:
                queue.append((node.right, row + 1, col + 1))
        
        result = []
        for col in sorted(column_table.keys()):
            column_vals = [val for row, val in sorted(column_table[col])]
            result.append(column_vals)
        
        return result