"""
给定一个整数数组，判断是否存在重复元素。

如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

 

示例 1:

输入: [1,2,3,1]
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""暴力求解，时间复杂度高"""
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         if len(nums) < 2:
#             return False
#
#         i = 0   # 慢指针
#         j = 1   # 快指针
#         for i in range(0, len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if nums[j] == nums[i]:
#                     return True
#         return False

"""先排序再查找"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2 :
            return False
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False

"""Python简单方法，利用set"""
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         return len(nums) != len(set(nums))


"""哈希表，即字典"""
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         dict = {}
#         for num in nums:
#             if num in dict.keys():
#                 return True
#             dict[num] = 0
#         return False