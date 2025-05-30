# Sliding Window Maximum

**Difficulty**: HARD

**URL**: [https://leetcode.com/problems/sliding-window-maximum/](https://leetcode.com/problems/sliding-window-maximum/)

---

# Sliding Window Maximum

**Difficulty**: Hard

**Tags**: Array, Queue, Sliding Window, Heap (Priority Queue), Monotonic Queue

---

You are given an array of integers&nbsp;nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

&nbsp;
Example 1:


Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


Example 2:


Input: nums = [1], k = 1
Output: [1]


&nbsp;
Constraints:


	1 &lt;= nums.length &lt;= 105
	-104 &lt;= nums[i] &lt;= 104
	1 &lt;= k &lt;= nums.length



