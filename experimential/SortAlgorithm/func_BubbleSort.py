# 冒泡排序

#单指针
def func_singlepointer(nums:list):
    if(len(nums)<=1):return
    for i in range(0,len(nums)-1):
        for j in range(0,len(nums)-1-i):
            if(nums[j]>nums[j+1]):
                nums[j]=nums[j]+nums[j+1]
                nums[j+1]=nums[j]-nums[j+1]
                nums[j]=nums[j]-nums[j+1]
# 双指针
def func_doublepointer(nums:list):
    if(len(nums)<=1):return
    for i in range(0,len(nums)-1):
        for j,k in zip(range(0,len(nums)-1-i),range(1,len(nums)-i)):
            if(nums[j]>nums[k]):
                nums[j]=nums[j]+nums[k]
                nums[k]=nums[j]-nums[k]
                nums[j]=nums[j]-nums[k]
# 递归
def func_recrusion(nums:list):
    # 底层返回
    if(len(nums)<=1):return
    # 排序
    for j in range(0,len(nums)-1):
        if(nums[j]>nums[j+1]):
            nums[j]=nums[j]+nums[j+1]
            nums[j+1]=nums[j]-nums[j+1]
            nums[j]=nums[j]-nums[j+1]
    # 调用自身
    func_recrusion(nums[0:len(nums)-1])
    # 顶层返回
    return
    


if __name__=="__main__":
    nums1=[0,-1,10,9,5,8,9,6,1]
    nums2=[10]
    nums3=[]
    func_singlepointer(nums1)
    print(nums1)
    func_singlepointer(nums2)
    print(nums2)
    func_singlepointer(nums3)
    print(nums3)
    func_doublepointer(nums1)
    print(nums1)
    func_doublepointer(nums2)
    print(nums2)
    func_doublepointer(nums3)
    print(nums3)
    func_recrusion(nums1)
    print(nums1)
    func_recrusion(nums2)
    print(nums2)
    func_recrusion(nums3)
    print(nums3)