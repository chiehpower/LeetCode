"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

Source from: LeetCode 
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        Reference: https://books.halfrost.com/leetcode/ChapterFour/0001~0099/0002.Add-Two-Numbers/ 
        """
        node = ListNode(0)
        n1, n2, carry, current = 0, 0, 0, node

        while l1 != None or l2 != None or carry != 0:
            if l1 != None:
                n1 = l1.val
                l1 = l1.next
            else:
                n1 = 0

            if l2 != None:
                n2 = l2.val
                l2 = l2.next
            else:
                n2 = 0

            current.next = ListNode((n1 + n2 + carry) % 10)
            current = current.next

            carry = int((n1 + n2 + carry) / 10)
        return node.next