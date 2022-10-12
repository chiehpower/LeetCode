"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""

class Solution:
    def maxDepth(self, root):
        """
        ref: https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/1769367/Python3-RECURSIVE-DFS-(-**-)-Explained
        Runtime: 51 ms, faster than 82.76% of Python3 online submissions for Maximum Depth of Binary Tree.
        Memory Usage: 16.4 MB, less than 23.40% of Python3 online submissions for Maximum Depth of Binary Tree.
        """
        def dfs(root, depth):
            if not root: return depth
            return max(dfs(root.left, depth+1), dfs(root.right, depth +1))
        return dfs(root, 0)
        
if __name__ == "__main__":
    Solution = Solution()

    root = [3,9,20,None,None,15,7]
    result = Solution.maxDepth(root)
    print(f"My ans is: {result}\n, Ans: 3")

    root = [1,None,2]
    result = Solution.maxDepth(root)
    print(f"My ans is: {result}\n, Ans: 2")
    

