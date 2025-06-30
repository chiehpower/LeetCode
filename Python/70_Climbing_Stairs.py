"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:

1 <= n <= 45

Source from: LeetCode 
"""


class Solution(object):
    """2022/03/27 23:12"""
    def climbStairs(self, n):
        """
        Reference: https://www.youtube.com/watch?v=Y0lT9Fck7qI&ab_channel=NeetCode
        Runtime: 24 ms, faster than 93.85% of Python3 online submissions for Climbing Stairs.
        Memory Usage: 13.9 MB, less than 7.13% of Python3 online submissions for Climbing Stairs.
        """      
        one, two = 1, 1
        for i in range(n- 1):
            
            temp = one
            one = one + two # F(n) = F(n-1) + F(n-2)
            two = temp

        return one

    def climbStairs_20250630(self, n):
        """
        Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Summary Ranges.
        Memory Usage: 17.63 MB, less than 21.82% of Python3 online submissions for Summary Ranges.
        """
        zero, one = 1, 1
        if n == 1:
            return one
        for i in range(1, n):
            new = zero + one
            zero = one
            one = new
        return new


Solution = Solution()

inputs = 2
target = 2

result = Solution.twoSum(inputs, target)
print(result) # Answer: 2