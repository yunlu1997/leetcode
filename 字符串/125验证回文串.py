"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""双指针，left and right"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            while left < len(s) and not s[left].isalnum():    # 左指针找到第一个字母
                left +=1
            while right > 0 and not s[right].isalnum():    # 右指针找到第一个字母
                right -=1
            if left > right:    # 指针相遇时返回True
                return True
            if s[left].upper() != s[right].upper():  # 不一样返回False,忽略大小写的话则统一成大写
                return False
            left +=1
            right -=1
        return True

"""利用正则表达式"""
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        return tmp == tmp[::-1]

"""
类似的思想，但不用正则
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_ = []
        i = len(s)-1
        while i >= 0:
           char = s[i]
           if char.isalnum():
               s_.append(char.lower())
           i-=1
        return s_ == s_[::-1]


