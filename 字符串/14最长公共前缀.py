"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        for i in zip(*strs):     # *strs 表示取出这个列表里的每个字符串
            if len(set(i))== 1 : # 有重复字符时， set的长度为1
                result += i[0]
            else:
                break # 当出现不重复时，跳出循环
        return result

