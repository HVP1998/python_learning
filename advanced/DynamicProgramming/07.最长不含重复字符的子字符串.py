'''
从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度
'''
"""
最优子结构

状态定义：
dp[i]   以pos为开头s[i]为结尾的字符串不含重复字符子字符串的长度
pos     与当前s[i]重合字符的后一个字符的位置
状态转移方程：
dp[i]=max(dp[i-1],dp[i])
pos=i   s[i]=s[j]

-------------------------------------------------------

答案精进：
状态定义：
dp[j]   以s[j]为结尾的字符串不含重复字符子字符串的长度
i       前一个与当前字符重复的字符位置
j       当前字符位置
状态转移方程：
dp[j]=dp[j-1]+1 j-i>dp[j-1]    
dp[j]=j-1       j-i<=dp[j-i]    

"""
class Solution:
    # 循环
    def lengthOfLongestSubstring1(self, s: str) -> int:
        if(len(s)<=1):return len(s)
        pos,max_length=0,1
        for i in range(1,len(s)):
            length=1
            for j in range(pos,i):
                if(s[i]==s[j]):
                    pos=j+1
                    break
                length+=1
            max_length=max(length,max_length)
        return max_length
    # 答案：动态规划+字典
    def lengthOfLongestSubstring2(self, s: str) -> int:
        if(len(s)<=1):return len(s)
        char,max_length=dict(),[0]*len(s)
        for j in range(0,len(s)):
            # 取上一个与字符s[j]重合的字符的位置
            i=char.get(s[j],-1)
            # 记录当前字符位置
            char[s[j]]=j
            if(j-i>max_length[j-1] and j-1>-1):max_length[j]=max_length[j-1]+1
            else:max_length[j]=j-i
        return max(max_length)
    # 答案：动态规划+遍历
    def lengthOfLongestSubstring3(self, s: str) -> int:
        res = tmp = i = 0
        for j in range(len(s)):
            i = j - 1
            while i >= 0 and s[i] != s[j]: i -= 1 # 线性查找 i
            tmp = tmp + 1 if tmp < j - i else j - i # dp[j - 1] -> dp[j]
            res = max(res, tmp) # max(dp[j - 1], dp[j])
        return res
    # 答案：动态规划+双指针迭代
    def lengthOfLongestSubstring4(self, s: str) -> int:
        dic, res, i = {}, 0, -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i) # 更新左指针 i
            dic[s[j]] = j # 哈希表记录
            res = max(res, j - i) # 更新结果
        return res

 
        



if __name__=="__main__":
    S=Solution()
    # print(S.lengthOfLongestSubstring1("abdcfgcabnvghcbb"))
    # print(S.lengthOfLongestSubstring2("abdcfgcabnvghcbb"))
    print(S.lengthOfLongestSubstring1("jsdnfkandaisuenfnefjksdkdjfnadsf"))
    print(S.lengthOfLongestSubstring4("abcba"))