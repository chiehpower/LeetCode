"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 
Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Summary Ranges.
        Memory Usage: 17.96 MB, less than 28.22% of Python3 online submissions for Summary Ranges.
        [Again]
        """
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        while i >= 0 or j >= 0 or carry:

            a_num = int(a[i]) % 2 if i >= 0 else 0
            b_num = int(b[j]) % 2 if j >= 0 else 0
        
            total = a_num + b_num + carry
            result.append(str(total % 2))
            carry = total // 2

            i -= 1
            j -= 1

        return ''.join(reversed(result))