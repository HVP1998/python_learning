'''




'''
def func_loop(nums:list):
    if(len(nums)<=1):return nums
    for i in range(1,len(nums)):
        tmp_insert_pos=i
        for j in range(i-1,-1,-1):
            if(nums[j]>nums[i]):
                tmp_insert_pos=j
        if(not tmp_insert_pos==i):
            for j in range(tmp_insert_pos,i):
                nums[j]=nums[j]+nums[i]
                nums[i]=nums[j]-nums[i]
                nums[j]=nums[j]-nums[i]
    return nums
def func_recrusion(nums:list):
    if(len(nums)<=1):return nums
    nums[0:len(nums)-1]=func_recrusion(nums[0:len(nums)-1])
    tmp_insert_pos=len(nums)-1
    for j in range(len(nums)-2,-1,-1):
        if(nums[j]>nums[len(nums)-1]):
            tmp_insert_pos=j
    if(not tmp_insert_pos==len(nums)-1):
        for j in range(tmp_insert_pos,len(nums)-1):
            nums[j]=nums[j]+nums[len(nums)-1]
            nums[len(nums)-1]=nums[j]-nums[len(nums)-1]
            nums[j]=nums[j]-nums[len(nums)-1]
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