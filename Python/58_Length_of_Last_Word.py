"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 
Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""

class Solution:
    def lengthOfLastWord_oneline(self, s: str) -> int:
        return len(s.strip().split()[-1]) if s.strip() else 0

    def lengthOfLastWord(self, s: str) -> int:
        word_len = 0
        last_len = 0
        for i in s:
            if i != " ":
                word_len += 1
                last_len = word_len
            else:
                word_len = 0
        return last_len


def run_tests():
    """
    Runtime: 3 ms, faster than 4.34% of Python3 online submissions for Length of Last Word.  
    Memory Usage: 17.71 MB, less than 61.07% of Python3 online submissions for Length of Last Word.
    """
    sol = Solution()
    test_cases = [
        ("Hello World", 5),
        ("   fly me   to   the moon  ", 4),
        ("luffy is still joyboy", 6),
        ("a", 1),
        ("day", 3),
        ("a ", 1),
        ("   ", 0),
        ("", 0),
        ("Today is a nice day", 3),
    ]
    
    for i, (input_str, expected) in enumerate(test_cases):
        result = sol.lengthOfLastWord(input_str)
        print(f"Test Case {i+1}: {'✅ Passed' if result == expected else f'❌ Failed (Expected {expected}, Got {result})'}")

run_tests()