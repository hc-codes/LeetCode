// Problem: Sort List
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/sort-list/
// Date: 2024-08-29

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        def findmid(h):
            slow=h
            fast=h.next
            while fast and fast.next:
                slow=slow.next
                fast=fast.next.next
            return slow
        
        def merge(lhead,rhead):
            dummy=ListNode(-1)
            temp=dummy
            while lhead and rhead:
                if lhead.val<rhead.val:
                    temp.next=lhead
                    temp=lhead
                    lhead=lhead.next
                else:
                    temp.next=rhead
                    temp=rhead
                    rhead=rhead.next
            temp.next=lhead if lhead else rhead
            return dummy.next
        
        mid=findmid(head)
        lhead=head
        rhead=mid.next
        mid.next=None
        lhead=self.sortList(lhead)
        rhead=self.sortList(rhead)
        return merge(lhead,rhead)
            