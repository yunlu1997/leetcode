"""
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

 

示例 1:

输入: [3,0,1]
输出: 2
示例 2:

输入: [9,6,4,2,3,5,7,0,1]
输出: 8
"""

"""
数学方法
先求0到n的和，再减去现有的，就得到了缺失值
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        summary = len(nums)*(len(nums)+1)//2
        return summary - sum(nums)


"""
先将所有数字加入一个set
然后依次查询是否在set中
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for i in range(len(nums)+1):
            if i not in nums_set:
                return i


