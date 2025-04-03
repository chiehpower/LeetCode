"""
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.

Example 2:

Input: s = "foo", t = "bar"

Output: false

Explanation:

The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:

Input: s = "paper", t = "title"

Output: true


Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Runtime: 3 ms, faster than 95.93% of Python3 online submissions for Summary Ranges.
        Memory Usage: 18.08 MB, less than 37.59% of Python3 online submissions for Summary Ranges.
        """
        t_count = {}
        for j in t:
            if j not in t_count:
                t_count[j] = None

        s_count = {}
        for k in range(len(t)):
            if t_count[t[k]] == None:
                if s[k] in s_count:
                    if s_count[s[k]] != t[k]:
                        return False
                t_count[t[k]] = s[k]
                s_count[s[k]] = t[k]
            else:
                if s[k] != t_count[t[k]]:
                    return False
        return True

