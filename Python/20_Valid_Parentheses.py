"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
class Solution:
    def isValid_20250405(self, s: str) -> bool:
        """
        Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Summary Ranges.
        Memory Usage: 17.73 MB, less than 81.06% of Python3 online submissions for Summary Ranges.
        """
        if len(s) == 1:
            return False
        stack = []
        mapping = {'{':'}', '[':']', '(':')'}
        for i in s:
            if i in mapping:
                stack.append(mapping[i])
            else:
                if stack:
                    top = stack.pop()
                    if top != i:
                        return False
                else:
                    return False
        if len(stack) != 0:
            return False 
        return True

    def isValid_20250406(self, s: str) -> bool:
        if len(s) == 1:
            return False

        stack = []
        mapping = {'{': '}', '(': ')', '[': ']'}

        for char in s:
            # check it is a left bracket or right bracket
            if char in mapping:
                # if it is a left bracket, then add a mapping bracket in the stack to check later
                stack.append(mapping[char])
            else:
                # if it is a right bracket and stack is valid
                if stack:
                    top = stack.pop()
                    if char != top:
                        return False
                else:
                    # there is nothing to check.
                    return False
        # check if stack is empty or not.
        if len(stack) != 0:
            return False
        return True