"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        先把每個字母排序，成為一個key，然後把能夠獲得相同key的字母放在一起
        Runtime: 12 ms, faster than 61.64% of Python3 online submissions for Summary Ranges.
        Memory Usage: 20.54 MB, less than 89.65% of Python3 online submissions for Summary Ranges.
        """
        if len(strs) == 1:
            return [strs]
        group_mapping = {}

        for word in strs:
            key = ''.join(sorted(word))
            if key not in group_mapping:
                group_mapping[key] = [word]
            else:
                group_mapping[key].append(word)
        return list(group_mapping.values())