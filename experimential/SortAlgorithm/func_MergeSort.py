# 归并排序


# 递归
def func_recrusion(nums:list)->list:
    # 底层返回
    if(len(nums)<=1):return nums
    # 调用自身
    nums[0:int(len(nums)/2)]=func_recrusion(nums[0:int(len(nums)/2)])
    nums[int(len(nums)/2):len(nums)]=func_recrusion(nums[int(len(nums)/2):len(nums)])
    # 排序
    nums1=nums[0:int(len(nums)/2)]
    nums2=nums[int(len(nums)/2):len(nums)]
    nums_new=[0]*len(nums)
    p1,p2=0,0
    for i in range(0,len(nums)):
        # 两个子数组都还有没有进行排序的元素
        if(p1<=len(nums1)-1)and(p2<=len(nums2)-1):
            if(nums1[p1]>nums2[p2]):
                nums_new[i]=nums2[p2]
                p2+=1
            else:
                nums_new[i]=nums1[p1]
                p1+=1
        elif(p1>len(nums1)-1)and(p2<=len(nums2)-1):
            nums_new[i:len(nums)]=nums2[p2:len(nums2)]
        elif(p1<=len(nums1)-1)and(p2>len(nums2)-1):
            nums_new[i:len(nums)]=nums1[p1:len(nums1)]
    return nums_new

if __name__=="__main__":
    nums1=[0,-1,10,9,5,8,9,6,1]
    nums2=[10]
    nums3=[]
    print(func_recrusion(nums1))
    print(func_recrusion(nums2))
    print(func_recrusion(nums3))