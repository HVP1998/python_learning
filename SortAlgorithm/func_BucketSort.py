# 桶排序。
# 算法:1.根据桶的个数确定桶的范围。2.遍历列表将列表中的参数放入相应的桶中。3.再每个桶中进行排序。4.将桶中的列表整合为一个列表
def BucketSort(nums,count):
    # 确定最大值最小值
    length=int(len(nums))
    max=nums[0]
    min=nums[0]
    for i in range(1,length,1):
        if(max<nums[i]):
            max=nums[i]
        elif(min>nums[i]):
            min=nums[i]
    # 设置桶
    step=(max+1-min)/count
    bucket=[]
    for i in range(0,count,1):
        bucket.append([])
        for j in range(0,len(nums),1):
            if((nums[j]>=min+i*step)and(nums[j]<min+(i+1)*step)):
                bucket[i].append(nums[j])
    nums_new=[]
    for i in range(0,len(bucket),1):
        for j in range(1,len(bucket[i]),1):
            for k in range(0,len(bucket[i])-j,1):
                if(bucket[i][k]>bucket[i][k+1]):
                    bucket[i][k]=bucket[i][k]+bucket[i][k+1]
                    bucket[i][k+1]=bucket[i][k]-bucket[i][k+1]
                    bucket[i][k]=bucket[i][k]-bucket[i][k+1]
        for j in range(0,len(bucket[i]),1):
            nums_new.append(bucket[i][j])
    return nums_new

if __name__=="__main__":
    print("****************************")
    nums=[76,85,84,79,80,82,80,79,78,78]
    # nums=[6,4,7,3,2,11,10,5,9,1,8]
    # nums=[2,1,5,3,6]
    count=5
    nums=BucketSort(nums,count)
    print(nums)
    