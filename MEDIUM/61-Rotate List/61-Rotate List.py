// Problem: Rotate List
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/rotate-list/
// Date: 2024-08-31

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        curr=head
        new_head=head
        nodes=[]
        c=0
        while curr:
            curr=curr.next
            c+=1
        k%=c
        print(k)
        curr=head
        while curr:
            pre=curr
            nodes.append(curr)
            curr=curr.next
            while k>0 and (not curr.next):
                pre=nodes.pop()
                print(pre.val)
                curr.next=new_head
                new_head=curr
                pre.next=None
                curr=pre
                k-=1
        return new_head
                