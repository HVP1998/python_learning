# class Solution:
#     def maxSubArray(self,nums:list[int])->int:
#         # 数组长度等于1直接返回
#         if(len(nums)==1):return nums[0]
#         # 数组预处理：将连续非负值求和
#         # sign=0     去除开头负值
#         # sign=1     当前值为非负值
#         # sign=-1    当前值为负值
#         # nums_new   将连续非负值求和后的数组
#         # pos        连续非负值开始的位置
#         # max_single 输入数组全为负时的数组最大值
#         # count      连续非负集合个数
#         nums_new,pos,sign,max_single,count=[],-1,0,nums[0],0
#         for i in range(0,len(nums)):
#             sum=0
#             # 负值
#             if(nums[i]<0):
#                 if(nums[i]>max_single):max_single=nums[i]
#                 # 数组开头非正值不进行预处理
#                 if(sign==0):
#                     continue
#                 # 记录连续非负值的和
#                 elif(sign==1):
#                     for j in range(pos,i):
#                         sum=sum+nums[j]
#                     nums_new.append(sum)
#                     pos,sign=i,-1
#             # 非负值 
#             else:
#                 # 记录第一个非负值的位置
#                 if(sign==0):
#                     pos,sign,count=i,1,count+1
#                 elif(sign==-1):
#                     for j in range(pos,i):
#                         sum=sum+nums[j]
#                     nums_new.append(sum) 
#                     pos,sign,count=i,1,count+1
#         # 若数组结尾为非负值需要再进行额外一次求和
#         if(nums[-1]>=0):
#             sum=0
#             for i in range(pos,len(nums)):
#                 sum=sum+nums[i]
#             nums_new.append(sum)
#         # 输入数组连续非负集合个数=0，直接输出最大值
#         if(count==0):return max_single
#         # 输入数组连续非负集合个数=1，直接输出求和数组第一项
#         elif(count==1):return nums_new[0]
#         # 输入数组连续非负集合个数>=2
#         else:
#             # max记录nums_new[i-1]
#             max,tmp,max_pos=nums_new[0],nums_new[0],0
#             for i in range(1,len(nums_new)-1,2):
#                 if(nums_new[i]+nums_new[i+1]>0 and nums_new[i-1]+nums_new[i]>0):
#                     if(max_pos==i-1):
#                         tmp=max+nums_new[i]+nums_new[i+1]
#                     else:
#                         tmp=nums_new[i-1]+nums_new[i]+nums_new[i+1]
#                 else:
#                     if(nums_new[i+1]>nums_new[i-1]):
#                         tmp=nums_new[i+1]
#                 if(tmp>max):max,max_pos=tmp,i+1
#                 tmp=nums_new[i+1]
#         return max
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)      


                




S=Solution()
# print(S.maxSubArray([-2,-6,-7,-1,0,-2]))              
# print(S.maxSubArray([-2,-6,0,12,5,7,-7,-1,-2]))              
# print(S.maxSubArray([2,6,7,1,0,2]))              
# print(S.maxSubArray([2,6,7,1,0,2,-10,-2,-5]))              
# print(S.maxSubArray([-10,-2,-5,2,6,7,1,0,2]))              
# print(S.maxSubArray([-2,-6,0,12,-5,7,7,-1,-2,10,1,-2,-5,1,5,2]))              
# print(S.maxSubArray([-2,-6,0,12,-5,7,7,-1,-2,10,1,-2,-5]))              
# print(S.maxSubArray([8,-19,5,-4,20]))              
# print(S.maxSubArray([2,-2,-2,0,-2,2,2]))  
# print(S.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  
print(S.maxSubArray([-9,-2,1,8,7,-6,4,9,-9,-5,0,5,-2,5,9,7]))  
            
