"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]

"""


# class Solution: # 时间o(k**n) 空间 o(1)
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         k_ = k % len(nums)
#         for i in range(k_): # 每次只移动一位，移动 k % n 次
#             last = nums[-1]  # 取出最后一位数字
#             for j in range(len(nums)): # 其余位置后移一位
#                 previous = nums[j]  # 先取出第j位置的数
#                 nums[j] = last  # 第j位的数等于前一位的数
#                 last = previous


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k_ = k % len(nums)
        nums[:] = nums[-k_:] + nums[0:-k_]
