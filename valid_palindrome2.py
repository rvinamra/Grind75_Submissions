# This is another interesting solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # Clean the string: convert to lowercase and remove non-alphanumeric characters
        cleaned_string = ''.join(char.lower() for char in s if char.isalnum())

        # Check if the cleaned string is equal to its reverse
        return cleaned_string == cleaned_string[::-1]
