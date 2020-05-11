"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/move-zeroes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""暴力解法，遍历数组"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for _ in range(len(nums)):
            if nums[i] == 0: # 如果当前位置是0，删除这个0，并将其加到最后，同时指针保持不动，以检查下一位
                del nums[i]
                nums.append(0)
            else:
                i += 1 # 当前位置不是0，指针后移一位
        return None


"""
双指针，快指针遍历数组，慢指针指向最新一个0元素的位置
第一次遇到非零元素，将非零元素与数组nums[0]互换，
第二次遇到非零元素，将非零元素与nums[1]互换，
第三次遇到非零元素，将非零元素与nums[2]，
以此类推，直到遍历完数组
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:    # 将非零元素与最新的零元素交换位置
                nums[i], nums[j] = nums[j], nums[i]
                i += 1  # 慢指针后移一位
        return None