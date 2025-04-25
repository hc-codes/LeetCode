# Check If a Word Occurs As a Prefix of Any Word in a Sentence

**Difficulty**: EASY

**URL**: [https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/](https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/)

---

# Check If a Word Occurs As a Prefix of Any Word in a Sentence

**Difficulty**: Easy

**Tags**: Two Pointers, String, String Matching

---

Given a sentence that consists of some words separated by a single space, and a searchWord, check if searchWord is a prefix of any word in sentence.

Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word. If searchWord is a prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.

A prefix of a string s is any leading contiguous substring of s.

&nbsp;
Example 1:


Input: sentence = &quot;i love eating burger&quot;, searchWord = &quot;burg&quot;
Output: 4
Explanation: &quot;burg&quot; is prefix of &quot;burger&quot; which is the 4th word in the sentence.


Example 2:


Input: sentence = &quot;this problem is an easy problem&quot;, searchWord = &quot;pro&quot;
Output: 2
Explanation: &quot;pro&quot; is prefix of &quot;problem&quot; which is the 2nd and the 6th word in the sentence, but we return 2 as it&#39;s the minimal index.


Example 3:


Input: sentence = &quot;i am tired&quot;, searchWord = &quot;you&quot;
Output: -1
Explanation: &quot;you&quot; is not a prefix of any word in the sentence.


&nbsp;
Constraints:


	1 &lt;= sentence.length &lt;= 100
	1 &lt;= searchWord.length &lt;= 10
	sentence consists of lowercase English letters and spaces.
	searchWord consists of lowercase English letters.



