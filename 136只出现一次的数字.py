"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


"""哈希表"""
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         dict = {}
#         for num in nums:
#             if num in dict.keys():
#                 dict[num] += 1
#             else:
#                 dict[num] = 1
#         for key, count in dict.items():
#             if count == 1:
#                return key


""" 
按位异或 xor 
a xor 0 = a, a xor a =0
XOR 满足交换律和结合律
a⊕b⊕a⊕c⊕c=(a⊕a)⊕b⊕(c⊕c)=0⊕b⊕0=b
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
         a = 0
         for i in range(len(nums)):
             a = a ^ nums[i]
         return a