# 计数排序。
# 算法：1.获得最大值最小值、确定计数范围、生成计数数组。2.
def CountingSort(nums):
    length=int(len(nums))
    max=nums[0]
    min=nums[0]
    for i in range(1,length,1):
        if(max<nums[i]):
            max=nums[i]
        elif(min>nums[i]):
            min=nums[i]
    nums_count=[0]*(max-min+1)
    nums_new=[0]*len(nums)
    for i in range(0,len(nums),1):
        nums_count[nums[i]-min]+=1
    # print(nums_count)
    for i in range(1,len(nums_count),1):
        nums_count[i]=nums_count[i-1]+nums_count[i]
    # print(nums_count)
    for i in range(len(nums)-1,-1,-1):
        nums_new[nums_count[nums[i]-min]-1]=nums[i]
        nums_count[nums[i]-min]-=1
    return nums_new
        

        

        
if __name__=="__main__":
    print("****************************")
    nums=[76,84,80,82,80,85]
    # nums=[6,4,7,3,2,11,10,5,9,1,8]
    # nums=[2,1,5,3,6]
    nums=CountingSort(nums)
    print(nums)
    