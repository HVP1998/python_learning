class Solution:
    def isNumber(self, s: str) -> bool:
        judge_matrix=[
            {" ":0,"s":1,"d":2,"n":9},
            {"d":2,"n":9},
            {"d":2,"n":3,"e":5," ":8},
            {"d":4,"e":5," ":8},
            {"d":4,"e":5," ":8},
            {"s":6,"d":7},
            {"d":7},
            {"d":7," ":8},
            {" ":8},
            {"d":4}

        ]
        p=0
        for i in range(0,len(s)):
            if(s[i]==" "):
                t=" "
            elif(s[i] in "+-"):
                t="s"
            elif("0"<=s[i]<="9"):
                t="d"
            elif(s[i]=="."):
                t="n"
            elif(s[i] in "eE"):
                t="e"
            else:
                t="?"
            if(not t in judge_matrix[p]):
                return False
            p=judge_matrix[p][t]
        if p in [2,3,4,7,8]:
            return True
        else:
            return False
S=Solution()
print(S.isNumber(".1."))