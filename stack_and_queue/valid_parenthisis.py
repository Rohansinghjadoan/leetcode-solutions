class Solution(object):
    def isValid(self, s):
        stack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                if not stack:
                    return False
                top = stack.pop()
                # \ is a line continue charactor
                if (i == ")" and top != "(") or \
                   (i == "]" and top != "[") or \
                   (i == "}" and top != "{"):
                    return False
        return len(stack) == 0
