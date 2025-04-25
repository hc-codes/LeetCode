# Count Items Matching a Rule

**Difficulty**: EASY

**URL**: [https://leetcode.com/problems/count-items-matching-a-rule/](https://leetcode.com/problems/count-items-matching-a-rule/)

---

# Count Items Matching a Rule

**Difficulty**: Easy

**Tags**: Array, String

---

You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:


	ruleKey == &quot;type&quot; and ruleValue == typei.
	ruleKey == &quot;color&quot; and ruleValue == colori.
	ruleKey == &quot;name&quot; and ruleValue == namei.


Return the number of items that match the given rule.

&nbsp;
Example 1:


Input: items = [[&quot;phone&quot;,&quot;blue&quot;,&quot;pixel&quot;],[&quot;computer&quot;,&quot;silver&quot;,&quot;lenovo&quot;],[&quot;phone&quot;,&quot;gold&quot;,&quot;iphone&quot;]], ruleKey = &quot;color&quot;, ruleValue = &quot;silver&quot;
Output: 1
Explanation: There is only one item matching the given rule, which is [&quot;computer&quot;,&quot;silver&quot;,&quot;lenovo&quot;].


Example 2:


Input: items = [[&quot;phone&quot;,&quot;blue&quot;,&quot;pixel&quot;],[&quot;computer&quot;,&quot;silver&quot;,&quot;phone&quot;],[&quot;phone&quot;,&quot;gold&quot;,&quot;iphone&quot;]], ruleKey = &quot;type&quot;, ruleValue = &quot;phone&quot;
Output: 2
Explanation: There are only two items matching the given rule, which are [&quot;phone&quot;,&quot;blue&quot;,&quot;pixel&quot;] and [&quot;phone&quot;,&quot;gold&quot;,&quot;iphone&quot;]. Note that the item [&quot;computer&quot;,&quot;silver&quot;,&quot;phone&quot;] does not match.

&nbsp;
Constraints:


	1 &lt;= items.length &lt;= 104
	1 &lt;= typei.length, colori.length, namei.length, ruleValue.length &lt;= 10
	ruleKey is equal to either &quot;type&quot;, &quot;color&quot;, or &quot;name&quot;.
	All strings consist only of lowercase letters.



