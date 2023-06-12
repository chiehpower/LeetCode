"""
You are given two strings word1 and word2. 
Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, 
append the additional letters onto the end of the merged string.

Return the merged string.

- Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

- Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

- Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d


Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.

Source from: LeetCode 


# Results: 
Runtime: 23 ms, faster than 22.56% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 13.3 MB, less than 97.82% of Python3 online submissions for Squares of a Sorted Array.


"""

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word1_length = len(word1)
        word2_length = len(word2)

        if word1_length == 1:
            return word1 + word2
        elif word2_length == 1:
            return word1[0] + word2 + word1[1:]
        
        samelength = min(word1_length, word2_length)
        new_word = ''
        for i in range(samelength):
            new_word += word1[i] + word2[i]
        
        if word1_length > samelength:
            new_word += word1[samelength:]
        elif word2_length > samelength:
            new_word += word2[samelength:]
        
        return new_word



if __name__ == "__main__":
    
    Solution = Solution()

    word1 = "abc"
    word2 = "pqr"
    
    result = Solution.mergeAlternately(word1, word2)
    print(f"My ans is: {result}\n")
    
    word1 = "ab"
    word2 = "pqrs"
    
    result = Solution.mergeAlternately(word1, word2)
    print(f"My ans is: {result}\n")