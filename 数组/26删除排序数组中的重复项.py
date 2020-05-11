"""
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
"""

class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0   # 慢指针
        for j in range(1, len(nums)):   # 快指针
            if nums[i] != nums[j]:  # 找到不相等的数，慢指针移动
                i += 1
                nums[i] = nums[j]
        return i+1


