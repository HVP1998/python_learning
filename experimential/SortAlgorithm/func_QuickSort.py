# 快速排序


# 递归
def func_recrusion(nums:list)->list:
    # 底层返回
    if(len(nums)<=1):return nums
    # 排序
    index,left,right_move=nums[0],0,True
    right=len(nums)-1
    while(not left==right):
        # 右指针左移
        if(right_move):
            if(nums[right]<index):
                nums[left]=nums[right]
                left+=1
                right_move=False
            else:
                right-=1
        # 左指针右移
        else:
            if(nums[left]>index):
                nums[right]=nums[left]
                right-=1
                right_move=True
            else:
                left+=1
    nums[left]=index
    # 调用自身
    nums[0:left]=func_recrusion(nums[0:left])
    nums[left+1:len(nums)]=func_recrusion(nums[left+1:len(nums)])
    # 顶层返回
    return nums


if __name__=="__main__":
    nums1=[0,8,-1,10,9,5,8,9,6,1]
    nums2=[10]
    nums3=[]
    func_recrusion(nums1)
    print(nums1)
    func_recrusion(nums2)
    print(nums2)
    func_recrusion(nums3)
    print(nums3)