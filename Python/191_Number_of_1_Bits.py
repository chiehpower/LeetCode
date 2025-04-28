"""
Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

Example 1:
Input: n = 11
Output: 3
Explanation:
The input binary string 1011 has a total of three set bits.

Example 2:
Input: n = 128
Output: 1
Explanation:
The input binary string 10000000 has a total of one set bit.

Example 3:
Input: n = 2147483645
Output: 30
Explanation:
The input binary string 1111111111111111111111111111101 has a total of thirty set bits.

Constraints:

1 <= n <= 231 - 1
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        Runtime: 2 ms, faster than 18.55% of Python3 online submissions for Summary Ranges.
        Memory Usage: 17.56 MB, less than 96.24% of Python3 online submissions for Summary Ranges.
        """
        count = 0
        while n:
            # 簡單說就是比較2進制的最後一位
            # if n & 1 == 1, count += 1
            # or n & 1 == 0, count += 0
            count += (n & 1)
            # 往右移一位
            n >>= 1
        
        return count

    def hammingWeight(self, n: int) -> int:
        """
        Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Summary Ranges.
        Memory Usage: 17.64 MB, less than 80.97% of Python3 online submissions for Summary Ranges.
        """
        # Brian Kernighan's Algorithm
        # 直接檢查最後一個出現1的位元
        # 有幾個1就加幾次直到n=0
        count = 0
        while n:
            n &= (n -1)
            count += 1
        return count 