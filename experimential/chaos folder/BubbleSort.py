'''




'''
def func_loop(nums:list):
    if(len(nums)<=1):return nums
    for i in range(0,len(nums)-1):
        for j in range(0,len(nums)-1-i):
            if(nums[j]>nums[j+1]):
                nums[j]=nums[j]+nums[j+1]
                nums[j+1]=nums[j]-nums[j+1]
                nums[j]=nums[j]-nums[j+1]
    return nums
def func_recrusion(nums:list):
    if(len(nums)<=1):return nums
    for j in range(0,len(nums)-1):
        if(nums[j]>nums[j+1]):
            nums[j]=nums[j]+nums[j+1]
            nums[j+1]=nums[j]-nums[j+1]
            nums[j]=nums[j]-nums[j+1]
    nums[0:len(nums)-1]=func_recrusion(nums[0:len(nums)-1])
    return nums

if __name__=="__main__":
    nums1=[0,1,-1,10,9,5,8,9,6,1]
    nums2=[10]
    nums3=[]
    print(func_loop(nums1))
    print(func_loop(nums2))
    print(func_loop(nums3))
    nums1=[0,1,-1,10,9,5,8,9,6,1]
    nums2=[10]
    nums3=[]
    print(func_recrusion(nums1))
    print(func_recrusion(nums2))
    print(func_recrusion(nums3))