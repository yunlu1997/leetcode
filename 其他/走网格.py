"""
有一个x*y的网格，只能从网格左上角走到右下角，计算一共有多少种走法
给定 int x 和 y
返回走法的数量 int
"""

"""
递归
"""
class Solution:
    def sumStep(self, x:int, y:int)-> int:
        if (x==1 and y==1): # 当行列都抵达终点时，返回0，代表没有路径了
            return 0
        if(x==1 or y==1):   # 当行列中有一个抵达终点时，返回1，代表只剩下一种路径
            return 1
        total = Solution.sumStep(self,x-1,y) + Solution.sumStep(self,x,y-1)
        return total


if __name__ == '__main__':
    solution = Solution()
    total = Solution.sumStep(solution,x=3,y=2)
    print(total)