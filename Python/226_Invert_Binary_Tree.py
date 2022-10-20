"""
Given the root of a binary tree, invert the tree, and return its root.

Example 1:

Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:

Input: root = [2,1,3]
Output: [2,3,1]

Example 3:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root):
        """
        Runtime: 44 ms, faster than 74.80% of Python3 online submissions for Invert Binary Tree.
        Memory Usage: 13.9 MB, less than 57.05% of Python3 online submissions for Invert Binary Tree.
        Ref: https://leetcode.com/problems/invert-binary-tree/discuss/62714/3-4-lines-Python
        """
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
