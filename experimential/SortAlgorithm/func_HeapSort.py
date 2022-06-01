# 堆排序


# 循环
def func_loop(nums:list):
    # 构造大根堆
    for i in range(1,len(nums)):
        if(nums[i]>nums[int((i-1)/2)]):
            nums[i]=nums[i]+nums[int((i-1)/2)]
            nums[int((i-1)/2)]=nums[i]-nums[int((i-1)/2)]
            nums[i]=nums[i]-nums[int((i-1)/2)]
    # 交换num[0]与num[len(nums)-1-j]
    for j in range(0,len(nums)-1):
        nums[0]=nums[0]+nums[len(nums)-1-j]
        nums[len(nums)-1-j]=nums[0]-nums[len(nums)-1-j]
        nums[0]=nums[0]-nums[len(nums)-1-j]
        # 构造大根堆
        for i in range(1,len(nums)-1-j):
            if(nums[i]>nums[int((i-1)/2)]):
                nums[i]=nums[i]+nums[int((i-1)/2)]
                nums[int((i-1)/2)]=nums[i]-nums[int((i-1)/2)]
                nums[i]=nums[i]-nums[int((i-1)/2)]

if __name__=="__main__":
    nums1=[0,-1,10,9,5,8,9,6,1]
    nums2=[10]
    nums3=[]
    func_loop(nums1)
    print(nums1)
    func_loop(nums2)
    print(nums2)
    func_loop(nums3)
    print(nums3)
