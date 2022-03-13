# 堆排序
def BigTree(nums):
    for i in range(1,len(nums),1):
        j=i
        while(True):
            if(nums[j]>nums[int((j-1)/2)]):
                nums[j]=nums[j]+nums[int((j-1)/2)]
                nums[int((j-1)/2)]=nums[j]-nums[int((j-1)/2)]
                nums[j]=nums[j]-nums[int((j-1)/2)]
            j=j-(j-int((j-1)/2))
            if(j<=0):
                break
    return nums
def HeapSort(nums):
    j=1
    for i in range(int(len(nums)-1),0,-1):
        nums[0]=nums[0]+nums[i]
        nums[i]=nums[0]-nums[i]
        nums[0]=nums[0]-nums[i]
        nums_new=nums[0:int(len(nums))-j:1]
        nums[0:int(len(nums))-j:1]=BigTree(nums_new)
        j+=1



if __name__=="__main__":
    nums=[6,4,7,3,2,11,10,5,9,1,8]
    BigTree(nums)
    HeapSort(nums)
    print(nums)
