"""
Given the root of a complete binary tree, return the number of the nodes in the tree.
According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
Design an algorithm that runs in less than O(n) time complexity.

Example 1:

Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:

Input: root = []
Output: 0

Example 3:

Input: root = [1]
Output: 1
 
Constraints:

The number of nodes in the tree is in the range [0, 5 * 104].
0 <= Node.val <= 5 * 104
The tree is guaranteed to be complete.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Summary Ranges.
        Memory Usage: 23.28 MB, less than 82.20% of Python3 online submissions for Summary Ranges.
        [Again]
        """
        if not root:
            return 0
        
        # 計算左邊與右邊的高度
        left_height = self.getHeight(root.left)
        right_height = self.getHeight(root.right)
        
        if left_height == right_height:
            return int(2 ** left_height) + self.countNodes(root.right)
        else:
            return int(2 ** right_height) + self.countNodes(root.left)

    def getHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height