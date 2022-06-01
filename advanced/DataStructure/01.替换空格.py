'''
请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
'''


class Solution:
    def replaceSpace(self, s: str) -> str:
        self.new_s = ""
        for i in range(0, len(s)):
            if(s[i] == " "):
                self.new_s = self.new_s+"%20"
            else:
                self.new_s = self.new_s+s[i]
        return(self.new_s)


if __name__ == "__main__":
    s = "sdf sdfsdf sdfsdf f"
    C = Solution()
    new_s = C.replaceSpace(s)
    print(new_s)
