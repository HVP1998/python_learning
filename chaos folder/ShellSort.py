'''




'''
def func_loop(nums:list)->list:
    if(len(nums)<=1):return nums
    d=int(len(nums)/2)
    while(d>=1):
        for i in range(0,d):
            for j in range(i,len(nums)-d,d):
                if(nums[j]>nums[j+d]):
                    nums[j]=nums[j]+nums[j+d]
                    nums[j+d]=nums[j]-nums[j+d]
                    nums[j]=nums[j]-nums[j+d]
        d=int(d/2)
    return nums

def func_recrusion(nums:list,d:int)->list:
    if(len(nums)<=1):return nums
    if(d==0):return nums
    for i in range(0,d):
        for j in range(i,len(nums)-d,d):
            if(nums[j]>nums[j+d]):
                nums[j]=nums[j]+nums[j+d]
                nums[j+d]=nums[j]-nums[j+d]
                nums[j]=nums[j]-nums[j+d]
    nums=func_recrusion(nums,int(d/2))
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
    print(func_recrusion(nums1,int(len(nums1)/2)))
    print(func_recrusion(nums2,int(len(nums1)/2)))
    print(func_recrusion(nums3,int(len(nums1)/2)))