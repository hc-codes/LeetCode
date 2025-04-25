// Problem: Big Countries
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/big-countries/
// Date: 2024-10-19

# Write your MySQL query statement below
select name,population,area from world where area>=3000000 or population >= 25000000