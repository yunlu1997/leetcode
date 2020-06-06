"""
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
"""

"""
暴力法
超出时间限制
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        res = 0
        for num in range(2,n):
            if Solution.isPrimes(self,num) == True:
                res += 1
        return res

    def isPrimes(self,num):
        for i in range(2, num):
            if num % i == 0:  # 如果被除了自身外的数整除，就不是质数
                return False
        return True

"""
暴力法的优化
i 不需要遍历到 n，而只需要到 sqrt(n) 即可。
依然超出时间限制
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        res = 0
        for num in range(2,n):
            if Solution.isPrimes(self,num) == True:
                res += 1
        return res

    def isPrimes(self,num):
        i = 2
        while i*i <= num:
            if num % i == 0:  # 如果被除了自身外的数整除，就不是质数
                return False
            i+=1
        return True


"""
效率提升的关键在于埃拉托斯特尼筛法，简称埃式筛，也叫厄拉多塞筛法：
【要得到自然数n以内的全部质数，只要把不大于根号n的所有质数的倍数剔除，剩下的就是质数。】
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        primes = [1]*n  # 先假定n个数全部是质数
        primes[0] = primes[1] = 0   # 1和2不是质数

        for i in range(2, int(n**0.5)+1):
            if primes[i] == 1:  # 只筛查质数
                primes[i*i:n:i] = [0] * len(primes[i*i:n:i])       # 将质数的倍数全部筛除出来，设为非质数
        return sum(primes)