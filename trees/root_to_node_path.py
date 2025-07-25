def get_path(root,target,path):
    if not root:
        return False
    path.append(root.val)
    if root.val== target:
        return True
    if (get_path(root.left,target,path)or (get_path(root.right,target,path))):
        return True
    path.pop()
    return False