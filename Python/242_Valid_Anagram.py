"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Source from: LeetCode 
"""
import time 

class Solution:
    def isAnagram(self, s, t):
        """
        Runtime: 69 ms, faster than 77.29% of Python3 online submissions for Valid Anagram.
        Memory Usage: 14.5 MB, less than 67.36% of Python3 online submissions for Valid Anagram.
        """
        
        word = {}
        for i in s:
            if i not in word:
                word[i] = 1
            else:
                word[i] += 1
        
        for ii in t:
            if ii not in word:
                return False
            else:
                if word[ii] < 1:
                    return False
                else:
                    word[ii] -= 1
        
        for i in word:
            if word[i] >= 1:
                return False
        
        return True
    
if __name__ == "__main__":
    Solution = Solution()  

    s = "anagram"
    t = "nagaram"
    start = time.time()
    result = Solution.isAnagram(s, t)
    print(result)

    print("Time :", time.time() - start)
    
    s = "rat"
    t = "cat"
    start = time.time()
    result = Solution.isAnagram(s, t)
    print(result)

    print("Time :", time.time() - start)
    
    s = "ab"
    t = "a"
    start = time.time()
    result = Solution.isAnagram(s, t)
    print(result)

    print("Time :", time.time() - start) 