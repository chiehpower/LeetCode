"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

Constraints:

-231 <= x <= 231 - 1
"""
class Solution:
    def reverse(self, x: int) -> int:
        """
        Runtime: 39 ms, faster than 59.52% of Python3 online submissions for Summary Ranges.
        Memory Usage: 17.95 MB, less than 83.12% of Python3 online submissions for Summary Ranges.
        """
        x_list = list(str(x))
        reversed_x_list = reversed(x_list)
        final = ''.join(reversed_x_list)
        if final[-1] == '-':
           final = '-' + final[:-1]
        final = int(final)
        if abs(final) > 2**31:
            return 0
        return final