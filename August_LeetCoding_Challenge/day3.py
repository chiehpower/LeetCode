"""
# Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

Constraints:

s consists only of printable ASCII characters.

Source from: LeetCode 
"""
import re

class Solution():
    def detectpalindrome(self, s):
        s = re.sub(r"[^a-zA-Z0-9]", "", s.lower())
        numb = len(s)
        if numb % 2 == 0:
            # this is even
            for i in range(numb//2):
                if s[i] != s[-(i+1)]:
                    return False
            return True
        else:
            # this is odd
            for i in range(numb//2):
                if s[i] != s[-(i+1)]:
                    return False
            return True

Solution = Solution()

### First one
inputs1 = "A man, a plan, a canal: Panama"
result = Solution.detectpalindrome(inputs1)
print(result) 
# True

### Second one
inputs2 = "race a car"
result = Solution.detectpalindrome(inputs2)
print(result)
# False

### Third one
inputs3 = "0P"
result = Solution.detectpalindrome(inputs3)
print(result)
# False


#### Update
# I think this way should work.
"""
class Solution():
    def detectpalindrome(self, s):
        s = re.sub(r"[^a-zA-Z0-9]", "", s.lower())
        numb = len(s)
        for i in range(numb//2):
            if s[i] != s[-(i+1)]:
                return False
        return True

"""