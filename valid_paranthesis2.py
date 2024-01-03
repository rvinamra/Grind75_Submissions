class Solution:
    def isValid(self, s: str) -> bool:
        
        # FASTER and BETTER solution from ChatGPT

        stack = []
        bracket_pairs = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_pairs.values():
                # If the character is an open bracket, push it onto the stack
                stack.append(char)
            elif char in bracket_pairs.keys():
                # If the character is a close bracket, check if it matches the top of the stack
                if not stack or stack.pop() != bracket_pairs[char]:
                    return False
            else:
                # Invalid character
                return False

        # The string is valid if the stack is empty at the end
        return not stack
