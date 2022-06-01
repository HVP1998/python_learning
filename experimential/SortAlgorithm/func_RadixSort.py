# 基数排序


def func_loop(nums:list)->list:
    if(len(nums)<=1):return nums
    # 寻找最长元素
    max_length=len(nums[0])
    for i in range(1,len(nums)):
        if(max_length<len(nums[i])):
            max_length=len(nums[i])
    # 将所有短于最长长度的元素在左边补'0'
    for i in range(0,len(nums)):
        if(len(nums[i])<max_length):
            nums[i]=(max_length-len(nums[i]))*"0"+nums[i]
    # 从每个元素的最右边的位进行比较开始排序(冒泡)
    for i in range(max_length-1,-1,-1):
        for j in range(0,len(nums)-1):
            for k in range(0,len(nums)-1-j):
                if(nums[k][i]>nums[k+1][i]):
                    nums[k],nums[k+1]=nums[k+1],nums[k]
    return nums
    

if __name__=="__main__":
    nums1=["0","1","10","19","5","8","9","6","1"]
    nums2=["10"]
    nums3=[]
    print(func_loop(nums1))
    print(func_loop(nums2))
    print(func_loop(nums3))