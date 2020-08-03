给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

"""
利用堆栈
从左至右遍历字符串，如果和栈顶对应则出栈，否则入栈
"""
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {"[":"]", "(":")", "{":"}","]":"[",")":"(","}":"{"}
        stack = []
        for char in s:
            if len(stack) != 0 and char == mapping[stack[-1]]:
                 stack.pop()
            else:
                stack.append(char)
        return(len(stack)==0)


"""
Python 字符串 
replace 方法
"""

class Solution:
    def isValid(self, s:str) -> bool:
        while '[]' in s or '()' in s or '{}' in s:
           s =  s.replace('[]'," ")
           s = s.replace('{}'," ")
           s =  s.replace("()"," ")
        return (s == " ")