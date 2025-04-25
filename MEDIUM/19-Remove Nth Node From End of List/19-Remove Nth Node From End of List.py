// Problem: Remove Nth Node From End of List
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
// Date: 2024-08-28

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return head
        fast=slow=head
        for _ in range(n):
            fast=fast.next
        if not fast:
            return head.next
        while fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return head