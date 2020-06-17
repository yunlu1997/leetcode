"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def reverse( x: int) -> int:
        temp_str = str(x)[::-1]
        if temp_str[-1] == '-':
            temp_str_ = '-' + temp_str[0:-1]
        else:
            temp_str_ = temp_str
        if int(temp_str_) < - 2**31 or int(temp_str_) > 2**31:
            return 0
        else:
            return int(temp_str_)


