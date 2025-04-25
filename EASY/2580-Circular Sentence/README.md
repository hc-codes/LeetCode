# Circular Sentence

**Difficulty**: EASY

**URL**: [https://leetcode.com/problems/circular-sentence/](https://leetcode.com/problems/circular-sentence/)

---

# Circular Sentence

**Difficulty**: Easy

**Tags**: String

---

A sentence is a list of words that are separated by a single space with no leading or trailing spaces.


	For example, &quot;Hello World&quot;, &quot;HELLO&quot;, &quot;hello world hello world&quot; are all sentences.


Words consist of only uppercase and lowercase English letters. Uppercase and lowercase English letters are considered different.

A sentence is circular if:


	The last character of each word in the sentence is equal to the first character of its next word.
	The last character of the last word is equal to the first character of the first word.


For example, &quot;leetcode exercises sound delightful&quot;, &quot;eetcode&quot;, &quot;leetcode eats soul&quot; are all circular sentences. However, &quot;Leetcode is cool&quot;, &quot;happy Leetcode&quot;, &quot;Leetcode&quot; and &quot;I like Leetcode&quot; are not circular sentences.

Given a string sentence, return true if it is circular. Otherwise, return false.

&nbsp;
Example 1:


Input: sentence = &quot;leetcode exercises sound delightful&quot;
Output: true
Explanation: The words in sentence are [&quot;leetcode&quot;, &quot;exercises&quot;, &quot;sound&quot;, &quot;delightful&quot;].
- leetcode&#39;s&nbsp;last character is equal to exercises&#39;s first character.
- exercises&#39;s&nbsp;last character is equal to sound&#39;s first character.
- sound&#39;s&nbsp;last character is equal to delightful&#39;s first character.
- delightful&#39;s&nbsp;last character is equal to leetcode&#39;s first character.
The sentence is circular.

Example 2:


Input: sentence = &quot;eetcode&quot;
Output: true
Explanation: The words in sentence are [&quot;eetcode&quot;].
- eetcode&#39;s&nbsp;last character is equal to eetcode&#39;s first character.
The sentence is circular.

Example 3:


Input: sentence = &quot;Leetcode is cool&quot;
Output: false
Explanation: The words in sentence are [&quot;Leetcode&quot;, &quot;is&quot;, &quot;cool&quot;].
- Leetcode&#39;s&nbsp;last character is not equal to is&#39;s first character.
The sentence is not circular.

&nbsp;
Constraints:


	1 &lt;= sentence.length &lt;= 500
	sentence consist of only lowercase and uppercase English letters and spaces.
	The words in sentence are separated by a single space.
	There are no leading or trailing spaces.



