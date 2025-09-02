"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string 
by deleting some (can be none) of the characters without 
disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 
Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 
Follow up: Suppose there are lots of incoming s, say s1, s2, ..., 
sk where k >= 109, and you want to check one by one to see if t has its subsequence. 
In this scenario, how would you change your code?
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Runtime 37ms Beats 89.00% of users with Python
        Memory 16.32MB Beats 62.68% of users with Python
        """
        s_total = len(s)
        t_total = len(t)
        if s_total == 0 and t_total == 0:
            return True
        elif s_total == 0 and t_total != 0:
            return True
        elif s_total != 0 and t_total == 0:
            return False

        if s_total == t_total:
            if s == t:
                return True
            else:
                return False
        
        c = 0
        for i in t:
            
            if i == s[c]:
                c += 1

                if c == s_total:
                    return True

        if c < (s_total-1):
            return False 

    def isSubsequence_20250902(self, s: str, t: str) -> bool:
        
        for i in t:
            if len(s) > 0:
                compare = s[0]
            else:
                return True
            if i == compare:
                if len(s) > 1:
                    s = s[1:]
                else:
                    s = ""
        if len(s) > 0:
            return False
        else:
            return True
            

if __name__ == "__main__":
    
    Solution = Solution()

    s = "abc"
    t = "ahbgdc"

    result = Solution.isSubsequence(s, t)
    print(f"My ans is: {result}\n")

    s = "axc"
    t = "ahbgdc"

    result = Solution.isSubsequence(s, t)
    print(f"My ans is: {result}\n")

    s = ""
    t = ""

    result = Solution.isSubsequence(s, t)
    print(f"My ans is: {result}\n")

    s = ""
    t = "ahbgdc"

    result = Solution.isSubsequence(s, t)
    print(f"My ans is: {result}\n")

    s = "ahbgdc"
    t = ""

    result = Solution.isSubsequence(s, t)
    print(f"My ans is: {result}\n")

    s = "bb"
    t = "ahbgdc"

    result = Solution.isSubsequence(s, t)
    print(f"My ans is: {result}\n")
