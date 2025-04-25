// Problem: Linked List Cycle II
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/linked-list-cycle-ii/
// Date: 2024-08-23

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        fast=head
        curr=head
        while fast and fast.next:
            curr=curr.next
            fast=fast.next.next
            if curr==fast:
                curr=head
                while curr != fast:
                    curr=curr.next
                    fast=fast.next
                return curr
        return None
            