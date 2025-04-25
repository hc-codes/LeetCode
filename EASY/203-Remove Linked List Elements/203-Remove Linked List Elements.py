// Problem: Remove Linked List Elements
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/remove-linked-list-elements/
// Date: 2024-08-22

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return
        head.next = self.removeElements(head.next, val)
        return head.next if head.val==val else head