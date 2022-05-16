"""
The complement of an integer is the integer you get 
when you flip all the 0's to 1's and all the 1's to 0's in 
its binary representation.

For example, The integer 5 is "101" in binary and 
its complement is "010" which is the integer 2.

Given an integer num, return its complement.

- Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 
(no leading zero bits), and its complement is 010. 
So you need to output 2.

- Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 
(no leading zero bits), and its complement is 0. So you need 
to output 0.


Constraints:

1 <= num < 2**31
 

Note: This question is the same as 1009: 
https://leetcode.com/problems/complement-of-base-10-integer/

Source from: LeetCode 


# Results: 
Runtime: 32 ms, faster than 55.58% of Python3 online submissions for Number Complement.
Memory Usage: 14.3 MB, less than 41.72% of Python3 online submissions for Number Complement.

Reference:
- Good solution: https://leetcode.com/problems/number-complement/discuss/96009/Simple-Python
"""


class Solution:
    def findComplement(self, num):
        # bin_num = bin(num)
        bin_num = format(num, "b")
        bin_num = bin_num.replace("1", "2")
        bin_num = bin_num.replace("0", "1")
        bin_num = bin_num.replace("2", "0")
        return int(bin_num, 2)


if __name__ == "__main__":
    
    Solution = Solution()

    num = 5
    
    result = Solution.findComplement(num)
    print(f"My ans is: {result}\n")

    num = 1
    
    result = Solution.findComplement(num)
    print(f"My ans is: {result}\n")