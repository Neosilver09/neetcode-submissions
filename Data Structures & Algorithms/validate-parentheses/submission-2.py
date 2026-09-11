class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dico = {')':'(', '}':'{',']':'['}
        for char in s:
            if char == ')' or char == '}' or char == ']' :
                check = stack.pop() if len(stack) != 0 else 0
                if check != dico.get(char):
                    return False
            else:
                stack.append(char)
        print(stack)
        return not stack

                

        