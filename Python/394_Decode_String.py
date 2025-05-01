"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""
class Solution:
    def decodeString(self, s: str) -> str:
        """
        Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Reverse Linked List II.
        Memory Usage: 17.79 MB, less than 44.21% of Python3 online submissions for Reverse Linked List II.
        [Again]
        """
        num_stack = []
        num_str = []
        current_num = 0
        current_str = ""
        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char.isalpha():
                current_str += char
            elif char == '[':
                num_stack.append(current_num)
                num_str.append(current_str)
                current_num = 0
                current_str = ""
            elif char == ']':
                num = num_stack.pop()
                previous_string = num_str.pop()
                current_str = previous_string + num * current_str

        return current_str