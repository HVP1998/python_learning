'''
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
'''
"""
利用阶乘进行分组
利用指针实现排列
缺点是时间过长  
执行用时：620ms在所有 Python3 提交中击败了5.01%的用户
内存消耗：18.9MB在所有 Python3 提交中击败了82.53%的用户
-----------------------------------------------------
答案精进：
利用DFS剪枝:遇到重复字符时不交换，直接跳过。省去遍历重复组合的时间。
交换原数据中字符的位置实现排列，不需要额外空间。
"""
from math import factorial
class Solution:
    # 利用阶乘分组
    def permutation_point(self, s: str) -> list[str]:
        def dfs(num:int,res:str,string:str,):
            # 当待处理字符串只有一个时返回
            if(len(string)==1):return res+string
            # 当前string进行分组时(n-1)!个数据一组 
            tmp=factorial(len(string)-1)
            # 通过整除确定是第几组
            res+=string[num//tmp]
            # 将被录入的字符串从待处理字符串中去除
            string=string[:num//tmp]+string[num//tmp+1:]
            # 在当前数据组中的序号
            num=num%tmp
            return dfs(num,res,string)
        if(len(s)==0):return [""]
        # 将结果设置为集合可以保证数据的非重复性
        res=set()
        # 循环记录数据总共有n!(n为数组长度)
        for i in range(factorial(len(s))):
            res.add(dfs(i,"",s))
        # 返回列表化数据
        return list(res)
    # 答案精进：两两交换寻找可能的组合
    def permutation_answer(self, s: str) -> list[str]:
        def dfs(num:int):
            if("".join(c) in dic):
                return 
            if(num==len(s)-1):
                dic.add("".join(c))
                res.append("".join(c))
                return 
            for i in range(num,len(s)):
                c[i],c[num]=c[num],c[i]
                dfs(num+1)
                c[i],c[num]=c[num],c[i]
            return 
        c=list(s)
        res,dic=list(),set()
        dfs(0)
        return res

if __name__=="__main__":
    S=Solution()
    print(S.permutation_answer("abb"))