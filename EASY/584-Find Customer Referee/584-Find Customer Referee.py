// Problem: Find Customer Referee
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/find-customer-referee/
// Date: 2024-10-19

# Write your MySQL query statement below
select name from customer where referee_id !=2 or referee_id is null