#插入排序 




# 双循环
def func_doubleloop(nums:list):
    if(len(nums)<=1):return
    for i in range(1,len(nums)):
        mark=i
        for j in range(0,i):
            if(nums[i]<nums[j]):
                mark=j
                break
        for j in range(mark,i):
            nums[i]=nums[i]+nums[j]
            nums[j]=nums[i]-nums[j]
            nums[i]=nums[i]-nums[j]
    return
# 递归
def func_recrusion(nums:list,len_nums:int):
    if(len(nums)<=1):return
    if(len_nums==len(nums)):return
    mark=len_nums
    for j in range(0,len_nums):
        if(nums[len_nums]<nums[j]):
            mark=j
            break
    for j in range(mark,len_nums):
        nums[len_nums]=nums[len_nums]+nums[j]
        nums[j]=nums[len_nums]-nums[j]
        nums[len_nums]=nums[len_nums]-nums[j]
    func_recrusion(nums,len_nums+1)
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
    func_recrusion(nums1,1)
    print(nums1)
    func_recrusion(nums2,1)
    print(nums2)
    func_recrusion(nums3,1)
    print(nums3)