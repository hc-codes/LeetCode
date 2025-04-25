// Problem: Merge Two Sorted Lists
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/merge-two-sorted-lists/
// Date: 2024-09-12

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        c1=list1
        c2=list2
        h=res=ListNode(-1)
        while c1 and c2:
            if c1.val<c2.val:
                res.next=c1
                res=res.next
                c1=c1.next
            else:
                res.next=c2
                c2=c2.next
                res=res.next
        while c1:
            res.next=c1
            c1=c1.next
            res=res.next
        while c2:
            res.next=c2
            c2=c2.next                
            res=res.next
        return h.next
                