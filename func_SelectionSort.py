def SelectionSort(nums):
    for i in range(0,len(nums)-1,1):
        max=nums[0]
        pos=0
        for j in range(1,len(nums)-i,1):
            if(max<nums[j]):
                max=nums[j]
                pos=j
        # 如果最大值位置不是当前序列的最高序位则将标记值与最大序位值进行交换
        if(not pos==len(nums)-1-i):
            # ex=nums[pos]
            # nums[pos]=nums[len(nums)-1-i]
            # nums[len(nums)-1-i]=ex
            nums[pos]=nums[len(nums)-1-i]+nums[pos]
            nums[len(nums)-1-i]=nums[pos]-nums[len(nums)-1-i]
            nums[pos]=nums[pos]-nums[len(nums)-1-i]

if __name__=="__main__":
    print("****************************")
    nums=[10,6,1,6,1,3,4,2]
    SelectionSort(nums)
    print(nums)