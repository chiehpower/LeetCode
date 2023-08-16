"""
Given a string s, reverse only all the vowels 
in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they 
can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "hello"
Output: "holle"

Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str

        
        Runtime 794ms Beats 18.65% of users with Python
        Memory 16.03mb Beats 36.95% of users with Python
        """

        target = ['a', 'e', 'i', 'o', 'u']
        reverse_list = []
        for i in s:
            if i.lower() in target:
                reverse_list.insert(0, i)
        
        new_list = []
        count = 0
        for i in s:
            if i.lower() in target:
                new_list.append(reverse_list[count])
                count += 1
            else:
                new_list.append(i)

        word = ""

        for i in new_list:
            word += i

        return word


if __name__ == "__main__":
    
    Solution = Solution()

    s = "hello"
    
    result = Solution.reverseVowels(s)
    print(f"My ans is: {result}\n")
    
    s = "leetcode"
    
    result = Solution.reverseVowels(s)
    print(f"My ans is: {result}\n")
