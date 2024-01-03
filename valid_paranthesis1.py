class Solution:
    def isValid(self, s: str) -> bool:
        
        end = [')', '}', ']']
        comp_pairs = {')' : '(',
                '}' : '{',
                ']' : '['}
        temp = []
        count = 0
        
        for char in s:
            if char not in end:
                temp.append(char)
                count += 1
            else:
                if count != 0 and comp_pairs[char] == temp[count-1]:
                    temp.pop(count-1)
                    count -= 1
                else:
                    return False

        if len(temp) == 0 and count == 0:
            return True
        else:
            return False
