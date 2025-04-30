"""
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701

Constraints:

- 1 <= columnTitle.length <= 7
- columnTitle consists only of uppercase English letters.
- columnTitle is in the range ["A", "FXSHRXW"].
"""
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """
        Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Summary Ranges.
        Memory Usage: 17.74 MB, less than 49.76% of Python3 online submissions for Summary Ranges.
        """
        total_len = len(columnTitle) - 1
        total_value = 0
        for i in columnTitle:
            total_value += (ord(i) - ord('A') + 1) * (26 ** total_len) 
            total_len -= 1
        return total_value