class Solution:
    # 1.暴力if法
    def strToInt1(self, str: str) -> int:
        # 初始化
        i = 0
        str_list = []
        # 确定第一个不是空格的字符位置
        while(i < len(str)):
            if(str[i] == " "):
                i += 1
            else:
                break
        # 如果全是空格返回0
        if(i== len(str)):
            return 0
        # 第一个非空格字符非符号或数字则表示非整数返回0
        if(str[i] in "+-"):
            str_list.append(str[i])
            i+=1
            if(i>=len(str)):
                return 0
            elif((str[i]>"9")or("0">str[i])):
                return 0
        elif("0" <= str[i] <= "9"):
            str_list.append(str[i])
            i+=1
            if(i>=len(str)):
                return int("".join(str_list))
        else:
            return 0
        # 字符串转换整数
        for j in range(i, len(str)):
            if("0" <= str[j] <= "9"):
                str_list.append(str[j])
            else:
                break
        # 将结果转换为整数
        res = int("".join(str_list))
        # 整数的输出范围为大于-2**31小于2**31-1
        if(res > 2**31-1):
            return 2**31-1
        elif(res < -2**31):
            return -2**31
        else:
            return res
    # 2.答案:每轮拼接判断是否超过上下限
    def strToInt2(self,str:str)->int:
        str = str.strip()                      # 删除首尾空格
        if not str: return 0                   # 字符串为空则直接返回
        res, i, sign = 0, 1, 1
        int_max, int_min, bndry = 2 ** 31 - 1, -2 ** 31, 2 ** 31 // 10
        if str[0] == '-': sign = -1            # 保存负号
        elif str[0] != '+': i = 0              # 若无符号位，则需从 i = 0 开始数字拼接
        for c in str[i:]:
            if not '0' <= c <= '9' : break     # 遇到非数字的字符则跳出
            if res > bndry or res == bndry and c > '7': return int_max if sign == 1 else int_min # 数字越界处理
            res = 10 * res + ord(c) - ord('0') # 数字拼接
        return sign * res


S = Solution()
print(S.strToInt1("+1"))
