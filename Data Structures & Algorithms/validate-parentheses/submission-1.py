class Solution:
    def isValid(self, s: str) -> bool:
        char_dict = {"(" : ")", "[" : "]", "{" : "}"}

        opening_paren = "({["
        stack = [] # lifo
        for char in s:
            if char in opening_paren:
                stack.append(char)
            elif len(stack) == 0 or char_dict[stack.pop()] != char:
                return False
            
        if len(stack) == 0:
            return True
        else:
            return False
