class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ['{','(', '[']:
                stack.append(i)
            elif i in ['}',')', ']']:
                if stack == []:
                    return False
                elif ord(i)- ord(stack.pop()) not in [1,2]:
                    return False                    
        if stack == []:
            return True
        return False