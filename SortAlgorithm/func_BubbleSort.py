# 冒泡排序
def BubbleSrt(nums):
    for i in range(1,len(nums)):
        for j in range(len(nums)-i):
            if(nums[j]>nums[j+1]):
                nums[j]=nums[j]+nums[j+1]
                nums[j+1]=nums[j]-nums[j+1]
                nums[j]=nums[j]-nums[j+1]

if __name__=="__main__":
    print("****************************")
    nums=[10,6,1,6,1,3,4,2]
    BubbleSrt(nums)
    print(nums)