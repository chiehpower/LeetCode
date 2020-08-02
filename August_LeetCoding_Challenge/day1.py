"""
# Detect Capital

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

1. All letters in this word are capitals, like "USA".
2. All letters in this word are not capitals, like "leetcode".
3. Only the first letter in this word is capital, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way.

# Example 1:

Input: "USA"
Output: True

# Example 2:

Input: "FlaG"
Output: False

Source from: LeetCode 
"""

class Solution:
    def detectCapitalUse(self, word):
        if word.isalpha() == True:
            if word.istitle() == True:
                return True
            elif word.isupper() == True:
                return True
            elif word.islower() == True:
                return True
            else:
                return False

Solution = Solution()

inputs = "USA"

result = Solution.detectCapitalUse(inputs)
print(result)