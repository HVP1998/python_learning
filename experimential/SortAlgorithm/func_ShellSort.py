# 希尔排序


# 双循环
def func_loop(nums:list):
    if(len(nums)<=1):return
    # 初始化间隔
    d=int(len(nums)/2)
    # 当步长小于1的时候退出循环
    while(d>=1):
        # 构造d个子列表
        for i in range(d):
            for j in range(i,len(nums)-d,d):
                if(nums[j]>nums[j+d]):
                    nums[j]=nums[j]+nums[j+d]
                    nums[j+d]=nums[j]-nums[j+d]
                    nums[j]=nums[j]-nums[j+d]
            print("")
        d=int(d/2)
# 递归
def func_recrusion(nums:list,d:int):
    if(len(nums)<=1):return nums
    # 底层返回
    if(d<1):return nums
    # 当步长小于1的时候退出循环
    for i in range(d):
        for j in range(i,len(nums)-d,d):
            if(nums[j]>nums[j+d]):
                nums[j]=nums[j]+nums[j+d]
                nums[j+d]=nums[j]-nums[j+d]
                nums[j]=nums[j]-nums[j+d]
    # 调用自身 顶层返回
    return func_recrusion(nums,int(d/2))
    

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
    func_recrusion(nums1,int(len(nums1)/2))
    print(nums1)
    func_recrusion(nums2,int(len(nums2)/2))
    print(nums2)
    func_recrusion(nums3,int(len(nums3)/2))
    print(nums3)