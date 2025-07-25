def all_tarversal(root):
    if not root:
        return []
    stack=[(root,1)]
    preorder, inorder,postorder=[],[],[]
    while stack:
        node,state=stack.pop()
        if state==1:
            preorder.append(node.val)
            stack.append((node,2))
            if node.left:
                stack.append((node.left,1))
            elif state==2:
                inorder.append((node.val))
                stack.append((node,3))
                if node.right:
                    stack.append(node.right,1)
            else:
                postorder.append(node.val)
    return preorder,inorder,postorder
