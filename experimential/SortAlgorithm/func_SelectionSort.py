# 选择排序


# 双循环
def func_doubleloop(nums:list):
    if(len(nums)<=1):return
    for i in range(0,len(nums)-1):
        max=nums[0]
        mark=0
        for j in range(1,len(nums)-i):
            if(max<nums[j]):max,mark=nums[j],j
        if(not mark==j):
            nums[mark]=nums[mark]+nums[j]
            nums[j]=nums[mark]-nums[j]
            nums[mark]=nums[mark]-nums[j]
# 递归
def func_recrusion(nums:list):
    # 底层返回
    if(len(nums)<=1):return
    # 排序
    max=nums[0]
    mark=0
    for j in range(1,len(nums)):
        if(max<nums[j]):max,mark=nums[j],j
    if(not mark==j):
        nums[mark]=nums[mark]+nums[j]
        nums[j]=nums[mark]-nums[j]
        nums[mark]=nums[mark]-nums[j]
    # 调用自身
    func_recrusion(nums[0:len(nums)-1])
    # 顶层返回
    return

if __name__=="__main__":
    nums1=[0,-1,10,9,5,8,9,6,1]
    nums2=[10]
    nums3=[]
    func_doubleloop(nums1)
    print(nums1)
    func_doubleloop(nums2)
    print(nums2)
    func_doubleloop(nums3)
    print(nums3)
    func_recrusion(nums1)
    print(nums1)
    func_recrusion(nums2)
    print(nums2)
    func_recrusion(nums3)
    print(nums3)