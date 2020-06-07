"""
给定一个整数，写一个函数来判断它是否是 3 的幂次方。

示例 1:

输入: 27
输出: true
示例 2:

输入: 0
输出: false
示例 3:

输入: 9
输出: true
示例 4:

输入: 45
输出: false
进阶：
你能不使用循环或者递归来完成本题吗？
"""

"""暴力法,超出时间"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(n):
            if 3**i == n:
                return True
        return False


"""
3^i = n
两边同时取 log3
i = log3(n) 只要是整数，说明n就是3的幂次方
"""
import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <=0:
            return False
        i = math.log10(n)/math.log10(3)     # 这里要用换底公式换成10的底，否则精度不够
        if i == int(i): # 如果i是整数，返回True
            return True
        else:
            return False


"""
循环
如果n是3的幂次方，那么会除到1，否则会除到一个小于1的数
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 1:
            n = n/3
        return n==1
