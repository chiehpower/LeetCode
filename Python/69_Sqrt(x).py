"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

Constraints:

0 <= x <= 231 - 1
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Runtime: 1432 ms, faster than 8.09% of Python3 online submissions for Summary Ranges.
        Memory Usage: 17.74 MB, less than 52.14% of Python3 online submissions for Summary Ranges.
        """
        
        min_values, min_v = 0, 0
        current  = 0
        while current <= x:
            current = min_v * min_v
            if current <= x:
                min_values = min_v
            else:
                return min_values
            min_v += 1
