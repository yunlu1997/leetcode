"""
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
"""

"""python 简单方法 利用str int list 之间的互相转换"""
# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         temp_str = ''.join([str(x) for x in digits])    # 先将list 转成 str
#         result_int = int(temp_str) + 1   # 将 str 转成 int 并加上 1
#         result = [int(x) for x in str(result_int)]  # 将上述结果 str 每一位转成list输出
#         return result

"""利用堆栈和进位标志"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        flag = 1    # 进位标志位
        while len(digits) > 0:
            temp = digits.pop() + flag # 出栈,进位或不进位取决于标志位
            if temp >= 10:  # 如果超出了10，需要再向前进位
                result.append(temp % 10)
                flag = 1    # 进位标志位设置为1
            else:
                result.append(temp)
                flag = 0   # 进位标志位设置为0
        if flag == 1:   # 如果到了第一位，仍需进位，则增加一个1
            result.append(flag)
        result.reverse()    # 需要反向
        return result
