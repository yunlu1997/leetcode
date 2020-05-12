"""
定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}
        """
        注意：
        用内置函数 collections.Counter(s) 也可以构建{字符：出现次数}的字典
        """
        for i in range(len(s)):
            if s[i] not in dict.keys(): # 字符作key, 出现的次数为value
                dict[s[i]] = 1
            else:
                dict[s[i]] += 1
        for i in range(len(s)):
            if dict[s[i]] == 1: # 在dict里找到数值为1的键
                return i
        return -1