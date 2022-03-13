# 快速排序
# 算法利用了分治的思想而且每次排序的方法相同可以利用递归
# 程序结构：1.最底层返回数据。2.排序。3.递归。4.返回排序后的数据
# 注意：现排序再递归
def QuickSort(nums):
    # 设置一个比较值
    index=nums[0]
    # 左标签位
    left=0
    # 右标签位
    right=len(nums)-1
    # 设置一个判断左标签还是右标签的标志
    switch="r"
    # 进行数组长度的循环，多一次是index赋值给指定位置
    for i in range(1,len(nums)+1,1):
        if(len(nums)<=1):
            return nums
        if(not left==right):
            if(switch=="r"):
                if(nums[right]<index):
                    nums[left]=nums[right]
                    left+=1 
                    switch="l"
                else:
                    right-=1   
            else:
                if(nums[left]>index):
                    nums[right]=nums[left]
                    right-=1
                    switch="r"
                else:
                    left+=1 
        else:
            nums[left]=index
    if(not left==0)and(not left==len(nums)-1):
        nums1=nums[0:left]
        nums2=nums[left+1:len(nums)]
        nums[0:left]=QuickSort(nums1)
        nums[left+1:len(nums)]=QuickSort(nums2)
    elif(left==0):
        nums3=nums[1:len(nums)]
        nums[1:len(nums)]=QuickSort(nums3)
    elif(left==len(nums)): 
        nums4=nums[0:len(nums)]
        nums[0:len(nums)]=QuickSort(nums4)   
    return nums 
    # 如果当前的数组长度小于等于2则不进行分组
if __name__=="__main__":
    print("****************************")
    nums=[6,4,7,3,2,10,5,9,1,8]
    QuickSort(nums)
    print(nums)
    