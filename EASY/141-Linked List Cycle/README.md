# Linked List Cycle

**Difficulty**: EASY

**URL**: [https://leetcode.com/problems/linked-list-cycle/](https://leetcode.com/problems/linked-list-cycle/)

---

# Linked List Cycle

**Difficulty**: Easy

**Tags**: Hash Table, Linked List, Two Pointers

---

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the&nbsp;next&nbsp;pointer. Internally, pos&nbsp;is used to denote the index of the node that&nbsp;tail&#39;s&nbsp;next&nbsp;pointer is connected to.&nbsp;Note that&nbsp;pos&nbsp;is not passed as a parameter.

Return&nbsp;true if there is a cycle in the linked list. Otherwise, return false.

&nbsp;
Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).


Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.


Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


&nbsp;
Constraints:


	The number of the nodes in the list is in the range [0, 104].
	-105 &lt;= Node.val &lt;= 105
	pos is -1 or a valid index in the linked-list.


&nbsp;
Follow up: Can you solve it using O(1) (i.e. constant) memory?


