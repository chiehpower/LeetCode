"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:

Input: n = 2
Output: false
 
Constraints:

1 <= n <= 231 - 1
"""
class Solution:
    def isHappy_20250405(self, n: int) -> bool:
        """
        Runtime: 1 ms, faster than 56.11% of Python3 online submissions for Summary Ranges.
        Memory Usage: 17.94 MB, less than 17.73% of Python3 online submissions for Summary Ranges.
        
        記錄是否看過這個總和數目，如果看過就是False
        """
        new_sum_values = 0
        seen = {}
        while new_sum_values != 1:
            for i in list(str(n)):
                new_sum_values += int(i) ** 2
            if new_sum_values == 1:
                return True

            if new_sum_values not in seen:
                seen[new_sum_values] = True
            else:
                return False
            n = new_sum_values
            new_sum_values = 0
        return True