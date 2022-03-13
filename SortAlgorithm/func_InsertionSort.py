# 插入排序
def InsertionSort(nums):
    for i in range(1,len(nums),1):
        num=nums[i]
        pos=i
        for j in range(i-1,-1,-1):
            if(num<nums[j]):
                pos=j
        # 记录需要交换的序列后将i位置的数据与标记序列依次交换
        if not pos==i:
            for k in range(pos,i,1):
                nums[i]=nums[k]+nums[i]
                nums[k]=nums[i]-nums[k]
                nums[i]=nums[i]-nums[k]
if __name__=="__main__":
    print("*******************************")
    nums=[10,6,1,6,1,3,4,2]
    InsertionSort(nums)
    print(nums)