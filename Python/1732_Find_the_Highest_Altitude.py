"""
There is a biker going on a road trip. The road trip consists of n + 1 
points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is 
the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). 
Return the highest altitude of a point.


Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

Example 2:

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
"""

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        record = [0]

        for i in gain:
            record.append(record[-1] + i)

        return max(record)

    def largestAltitude_20250813(self, gain: List[int]) -> int:
        highest = []
        curr = 0
        for i in gain:
            curr += i
            highest.append(curr)
        return max(highest) if max(highest) >= 0 else 0

    def largestAltitude_20250905(self, gain: List[int]) -> int:
        max_value = 0
        current = 0
        for i in gain:
            current += i
            max_value = max(max_value, current)
        return max_value

if __name__ == "__main__":
    
    Solution = Solution()

    gain = [-5,1,5,0,-7]

    result = Solution.largestAltitude(gain)
    print(f"My ans is: {result}\n")
    
    gain = [-5,1,5,0,-7]
        
    result = Solution.largestAltitude(gain)
    print(f"My ans is: {result}\n")
    
    gain = [-5,1,5,0,-7]

    result = Solution.largestAltitude(gain)
    print(f"My ans is: {result}\n")
