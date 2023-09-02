"""
Given a string s and an integer k, return the maximum 
number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 
Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
1 <= k <= s.length
"""
class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int

        Time limit exceeded
        """
        
        vowels = ['a', 'e', 'i', 'o', 'u']

        a = s[:k]
        max_number = 0
        for i in a:
            if i == 'a': max_number += 1
            if i == 'e': max_number += 1
            if i == 'i': max_number += 1
            if i == 'o': max_number += 1
            if i == 'u': max_number += 1
        
        for ii in s[k:]:
            a = a[1:] + str(ii)
            count = 0
            for i in a:
                if i == 'a': count += 1
                if i == 'e': count += 1
                if i == 'i': count += 1
                if i == 'o': count += 1
                if i == 'u': count += 1
            if count > max_number:
                max_number = count
        return max_number
