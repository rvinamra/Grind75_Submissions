import re
import math

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # removing the non-alphanumeric characters
        raw_string = re.sub(r'[^a-zA-Z0-9]', '', s)
        raw_string = raw_string.lower()

        is_palindrome = True

        if len(raw_string) == 0:
            return is_palindrome
        else:
            letters = len(raw_string)
            for char in range(0, int(len(raw_string)/2)):
                # checking if the chars match at both the ends
                if raw_string[char] != raw_string[letters-1]:
                    return False
                else:
                    letters -= 1
        

        return is_palindrome
