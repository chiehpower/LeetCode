"""
Given an array of integers arr, return true if the number of occurrences 
of each value in the array is unique or false otherwise.


Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. 
No two values have the same number of occurrences.

Example 2:

Input: arr = [1,2]
Output: false

Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        oc = {}

        for i in arr:
            if i not in oc:
                oc[i] = 1
            else:
                oc[i] += 1
        
        check = []
        for j in oc:
            check.append(oc[j])
        
        total_check = len(check)
        check_set = len(set(check))

        if total_check != check_set:
            return False
        else:
            return True

    def uniqueOccurrences_20250818(self, arr: List[int]) -> bool:
        seen = {}

        for i in arr:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1
        all_values = [seen[i] for i in seen]
        check = True if len(all_values) == len(list(set(all_values))) else False
        return check

if __name__ == "__main__":
    
    Solution = Solution()
    
    arr = [1,2,2,1,1,3]

    result = Solution.uniqueOccurrences(arr)
    print(f"My ans is: {result}\n")

    arr = [1,2]

    result = Solution.uniqueOccurrences(arr)
    print(f"My ans is: {result}\n")
    
    arr = [-3,0,1,-3,1,1,1,-3,10,0]

    result = Solution.uniqueOccurrences(arr)
    print(f"My ans is: {result}\n")