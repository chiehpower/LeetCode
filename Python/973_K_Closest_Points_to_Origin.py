"""
Given an array of points where points[i] = [xi, yi] 
represents a point on the X-Y plane and an integer k, 
return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is 
the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. 
The answer is guaranteed to be unique (except for the order that it is in).

- Example 1:

Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

- Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.

Source from: LeetCode 


# Results: 
Runtime: 2236 ms, faster than 5.01% of Python3 online submissions for K Closest Points to Origin.
Memory Usage: 50.1 MB, less than 9.07% of Python3 online submissions for K Closest Points to Origin.

Reference:
- Good solution: https://leetcode.com/problems/k-closest-points-to-origin/discuss/1647325/Python3-ONE-LINER-Explained
"""
# import math
from scipy.spatial import distance

class Solution:
    def kClosest(self, points, k):
        
        dis_list = []
        for i, point in enumerate(points):
            # distance = math.dist([point[0], point[1]], [0, 0])
            eu_distance = distance.euclidean((point[0], point[1]), (0, 0))
            dis_list.append([eu_distance, i])
        
        dis_list.sort()
        dis_list = dis_list[:k]

        for j in range(len(dis_list)):
            dis_list[j] = points[dis_list[j][1]]

        return dis_list
            
        


if __name__ == "__main__":
    Solution = Solution()

    points = [[1,3],[-2,2]]
    k = 1
    
    result = Solution.kClosest(points, k)
    print(f"My ans is: {result}\n")

    points = [[3,3],[5,-1],[-2,4]]
    k = 2
    
    result = Solution.kClosest(points, k)
    print(f"My ans is: {result}\n")
