class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        # 1.字符串切片
        return s[n:len(s):1]+s[0:n:1]
        # 2.字符串遍历拼接
        # res=[]
        # for i in range(n,len(s)):
        #     res.append(s[i])
        # for i in range(n):
        #     res.append(s[i])
        # return "".join(res)
        # 利用求余运算可以简化
        # res=[]
        # for i in range(n,n+len(s)):
        #     res.append(s[i%len(s)])
        # return "".join(res)
        # 3.列表遍历拼接
        # res=""
        # for i in range(n,len(s)):
        #     res=res+s[i]
        # for i in range(n):
        #     res=res+s[i]
        # return res
        # 利用求余运算可以简化
        # res=""
        # for i in range(n,n+len(s)):
        #     res=res+s[i%len(s)]
        # return res
        # 上述方法中由于字符串的不可变性：每次改变字符串的值都是新建了一个字符串。导致最后一种方法空间复杂度大
S=Solution()
print(S.reverseLeftWords("1234567",6))