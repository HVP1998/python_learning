# 桶排序


def func_loop(nums:list,count:int)->list:
    if(len(nums)<=1):return nums
    # 确定数组范围
    max,min=nums[0],nums[0]
    for i in range(1,len(nums)):
        if(max<nums[i]):max=nums[i]
        elif(min>nums[i]):min=nums[i]
    # 构造桶
    step=(max-min)/count
    bucket=list()
    for i in range(0,count):
        bucket.append([])
    # 将元素分类
    for i in range(0,len(nums)):
        if(nums[i]==max):
            bucket[count-1].append(nums[i])
            continue
        bucket[int((nums[i]-min)/step)].append(nums[i])
    # 每个桶内排序
    for i in range(count):
        for j in range(0,len(bucket[i])-1):
            for k in range(0,len(bucket[i])-1-j):
                if(bucket[i][k]>bucket[i][k+1]):
                    bucket[i][k]=bucket[i][k]+bucket[i][k+1]
                    bucket[i][k+1]=bucket[i][k]-bucket[i][k+1]
                    bucket[i][k]=bucket[i][k]-bucket[i][k+1]
    nums=[]
    for i in range(count):
        if(bucket[i]):
            for j in range(len(bucket[i])):
                nums.append(bucket[i][j])
    return nums    

if __name__=="__main__":
    nums1=[0,-1,10,9,5,8,9,6,1]
    nums2=[10]
    nums3=[]
    print(func_loop(nums1,5))
    print(func_loop(nums2,5))
    print(func_loop(nums3,5))