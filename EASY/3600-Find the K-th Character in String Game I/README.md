# Find the K-th Character in String Game I

**Difficulty**: EASY

**URL**: [https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/](https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/)

---

# Find the K-th Character in String Game I

**Difficulty**: Easy

**Tags**: Math, Bit Manipulation, Recursion, Simulation

---

Alice and Bob are playing a game. Initially, Alice has a string word = &quot;a&quot;.

You are given a positive integer k.

Now Bob will ask Alice to perform the following operation forever:


	Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.


For example, performing the operation on &quot;c&quot; generates &quot;cd&quot; and performing the operation on &quot;zb&quot; generates &quot;zbac&quot;.

Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.

Note that the character &#39;z&#39; can be changed to &#39;a&#39; in the operation.

&nbsp;
Example 1:


Input: k = 5

Output: &quot;b&quot;

Explanation:

Initially, word = &quot;a&quot;. We need to do the operation three times:


	Generated string is &quot;b&quot;, word becomes &quot;ab&quot;.
	Generated string is &quot;bc&quot;, word becomes &quot;abbc&quot;.
	Generated string is &quot;bccd&quot;, word becomes &quot;abbcbccd&quot;.



Example 2:


Input: k = 10

Output: &quot;c&quot;


&nbsp;
Constraints:


	1 &lt;= k &lt;= 500



