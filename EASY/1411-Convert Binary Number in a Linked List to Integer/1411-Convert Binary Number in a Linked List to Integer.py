// Problem: Convert Binary Number in a Linked List to Integer
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
// Date: 2024-08-21

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head:
            return 0
        curr=head
        res=0
        while curr:
            res=2*res + curr.val
            curr=curr.next
        return res
            