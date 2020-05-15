"""
「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 被读作  "one 1"  ("一个一") , 即 11。
11 被读作 "two 1s" ("两个一"）, 即 21。
21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。

给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。

注意：整数序列中的每一项将表示为一个字符串。
"""

"""递归"""
class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 1:
            return '1'
        pre = self.countAndSay(n-1) # 得到前一个str
        result = ''
        count = 1
        for i in range(len(pre)):
           if i == 0:
               count = 1
           elif pre[i] != pre[i-1]: # 如果前后两个字符不一样，则得到count+num, 同时count置为1
               temp = str(count)+pre[i-1]
               result += temp
               count = 1

           elif pre[i] == pre[i-1]: # 如果前后两个字符一样，则count+1
               count += 1

           if i == len(pre) - 1:  # 到str的最后一位时，要特殊处理
               temp = str(count) + pre[i]
               result += temp

        return result





