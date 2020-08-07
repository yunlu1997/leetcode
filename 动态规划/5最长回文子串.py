"""
5. 最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
通过次数338,207
"""


"""
p(i,j)代表从i到j的字符串
si 代表第i个位置的字符
dp方程： p(i,j) = p(i+1,j-1)^(Si==Sj)
边界条件：p(i,i) = True
          p(i,i+1) = (Si==Si+1)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        res=""
        for l in range(n):   # l为字符串长度
            for i in range(n):
                j = l+i
                if j >= len(s):
                    break
                elif l==0:    # 边界条件1
                    dp[i][j] = True
                elif l==1:
                    dp[i][j] = (s[i]==s[j]) # 边界条件2
                else:
                    dp[i][j] = dp[i+1][j-1] and (s[i]==s[j])
                if dp[i][j] and l >= len(res):
                    res = s[i:j+1]  # 因为前闭后开，因此必须要j+1
        return res