// Problem: Count Items Matching a Rule
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/count-items-matching-a-rule/
// Date: 2024-08-20

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        rule=0 if ruleKey=="type" else 1 if ruleKey=="color" else 2
        res=0
        for i in items:
            if i[rule]==ruleValue:
                res+=1
        return res