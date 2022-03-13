# 希尔排序
# 需要先进性排序再由排序后的列表组成新的列表进行排序。
# 程序结构：1.最底层数据返回。2.排序。3.递归。4.数据返回。
def ShellSort(nums,d):
    if(d==0):
        return nums
    for i in range(0,d,1):
        nums_new=nums[i:len(nums):d]
        for j in range(0,int(len(nums_new))-1,1):
            for k in range(0,int(len(nums_new))-1-j,1):
                if(nums_new[k]>nums_new[k+1]):
                    nums_new[k]=nums_new[k]+nums_new[k+1]
                    nums_new[k+1]=nums_new[k]-nums_new[k+1]
                    nums_new[k]=nums_new[k]-nums_new[k+1]
        nums[i:len(nums):d]=nums_new
    nums=ShellSort(nums,int(d/2))
    return nums


        

        
if __name__=="__main__":
    print("****************************")
    nums=[6,4,7,3,2,11,10,5,9,1,8]
    # nums=[2,1,5,3,6]
    nums=ShellSort(nums,int(len(nums)/2))
    print(nums)
    