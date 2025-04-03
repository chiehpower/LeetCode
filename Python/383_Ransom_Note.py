"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Runtime: 27 ms, faster than 27.41% of Python3 online submissions for Summary Ranges.
        Memory Usage: 18.05 MB, less than 35.32% of Python3 online submissions for Summary Ranges.
        """
        # 先個別把各自的數量都算出來
        # 最後只要magazine有小於ransomNote所需的數量，或者沒有的字，就是False
        ransomNote_seen = {}
        magazine_seen = {}

        for i in ransomNote:
            if i not in ransomNote_seen:
                ransomNote_seen[i] = 1
            else:
                ransomNote_seen[i] += 1

        for j in magazine:
            if j not in magazine_seen:
                magazine_seen[j] = 1
            else:
                magazine_seen[j] += 1

        for k in ransomNote_seen:

            if k not in magazine_seen:
                return False
            
            if k in magazine_seen:
                if magazine_seen[k] < ransomNote_seen[k]:
                    return False

        return True