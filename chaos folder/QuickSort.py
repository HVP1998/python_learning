'''




'''
# def func_loop(nums:list):

def func_recrusion(nums:list):
    if(len(nums)<=1):return nums
    index,left,right,right_move=nums[0],0,len(nums)-1,True
    while(not left==right):
        if(right_move):
            if(nums[right]<index):
                nums[left]=nums[right]
                right_move=False
                left+=1
            else:
                right-=1
        else:
            if(nums[left]>index):
                nums[right]=nums[left]
                right_move=True
                right-=1
            else:
                left+=1
    nums[left]=index
    nums[0:left]=func_recrusion(nums[0:left])
    nums[left+1:len(nums)]=func_recrusion(nums[left+1:len(nums)])
    return nums

if __name__=="__main__":
    # nums1=[0,1,-1,10,9,5,8,9,6,1]
    # nums2=[10]
    # nums3=[]
    # print(func_loop(nums1))
    # print(func_loop(nums2))
    # print(func_loop(nums3))
    nums1=[0,1,-1,10,9,5,8,9,6,1]
    nums2=[10]
    nums3=[]
    print(func_recrusion(nums1))
    print(func_recrusion(nums2))
    print(func_recrusion(nums3))