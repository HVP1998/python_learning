# 归并排序
# 算法利用了分治的思想而且每次排序的方法相同可以利用递归
# 程序结构：1.最底层返回数据。2.递归。3.排序。4.返回排序后的数据
# 注意：先递归再排序
def MergeSort(nums):
    if int(len(nums))==1:
        return nums
    d=int(len(nums)/2)
    nums1=MergeSort(nums[0:d:1])
    nums2=MergeSort(nums[d:int(len(nums)):1])
    p1=0
    p2=0
    p=0
    for i in range(0,int(len(nums)),1):
        if(p1==int(len(nums1))):
            nums[p:int(len(nums)):1]=nums2[p2:int(len(nums2)):1]
        elif(p2==int(len(nums2))):
            nums[p:int(len(nums)):1]=nums1[p1:int(len(nums1)):1]
        else:
            if(nums1[p1]>nums2[p2]):
                nums[p]=nums2[p2]
                p+=1
                p2+=1
            elif(nums1[p1]<nums2[p2]):
                nums[p]=nums1[p1]
                p+=1
                p1+=1
            else:
                nums[p]=nums2[p2]
                p+=1
                p2+=1
                nums[p]=nums1[p1]
                p+=1
                p1+=1
    return nums
if __name__=="__main__":
    nums=[6,4,7,3,2,10,5,9,1,8]
    MergeSort(nums)
    print(nums)