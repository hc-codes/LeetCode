// Problem: Middle of the Linked List
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/middle-of-the-linked-list/
// Date: 2024-08-23

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        slow=head
        fast=head
        c=1
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            c+=1
            print(slow.val)
        return slow