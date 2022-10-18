"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        """
        Runtime: 69 ms, faster than 44.48% of Python3 online submissions for Reverse Linked List.
        Memory Usage: 15.5 MB, less than 55.12% of Python3 online submissions for Reverse Linked List.
        
        Ref: https://leetcode.com/problems/reverse-linked-list/discuss/58127/Python-Iterative-and-Recursive-Solution
        """
        if head == None: return head
        prev = None
        while head:
            current = head 
            head = head.next
            current.next = prev
            prev = current
            
        return current
