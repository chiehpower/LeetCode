"""
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        Runtime: 3 ms, faster than 88.26% of Python3 online submissions for Spiral Matrix.
        Memory Usage: 17.72 MB, less than 63.51% of Python3 online submissions for Spiral Matrix.
        """
        if x < 0:
            return False
        if x == 0:
            return True
        word = str(x)
        new_word = ""
        for i in word:
            new_word = i + new_word
        if word != new_word:
            return False
        else:
            return True