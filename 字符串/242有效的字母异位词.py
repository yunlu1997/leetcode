"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-anagram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""用两个字典， 字符: 出现次数"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for i in range(len(s)):     # 将 s 中的字符及出现次数加入字典
            if s[i] not in dict_s.keys():
                dict_s[s[i]] = 1
            else:
                dict_s[s[i]] += 1
        for i in range(len(t)):     # 将 t 中的字符及出现次数加入字典
            if t[i] not in dict_t.keys():
                dict_t[t[i]] = 1
            else:
                dict_t[t[i]] += 1

        if dict_s.keys() != dict_t.keys():  # 首先判断是否出现的字符一样
            return False
        else:
            for key in dict_s.keys():       # 再判断每个字符出现的次数是否一样
                if dict_s[key] != dict_t[key]:
                    return False
        return True

"""字符串排序后判断是否相等"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
