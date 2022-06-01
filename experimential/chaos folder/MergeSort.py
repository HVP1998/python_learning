'''




'''
# def func_loop(nums:list)->list:
#     if(len(nums)<=1):return nums
#     for i in range(0,len(nums)-1):
#         for j in range(1,len(nums)-i):
#             for k in range(1,j+1):
#                 if(nums[k]>nums[int((k-1)/2)]):
#                     nums[k]=nums[k]+nums[int((k-1)/2)]
#                     nums[int((k-1)/2)]=nums[k]-nums[int((k-1)/2)]
#                     nums[k]=nums[k]-nums[int((k-1)/2)]
#         nums[0]=nums[0]+nums[len(nums)-1-i]
#         nums[len(nums)-1-i]=nums[0]-nums[len(nums)-1-i]
#         nums[0]=nums[0]-nums[len(nums)-1-i]
#     return nums

def func_recrusion(nums:list)->list:
    if(len(nums)<=1):return nums
    nums[0:int(len(nums)/2)]=func_recrusion(nums[0:int(len(nums)/2)])
    nums[int(len(nums)/2):len(nums)]=func_recrusion(nums[int(len(nums)/2):len(nums)])
    nums1=nums[0:int(len(nums)/2)]
    nums2=nums[int(len(nums)/2):len(nums)]
    p1,p2,i=0,0,0
    while(True):
        if(p1==len(nums1) and p2==len(nums2)):
            break
        elif(p1==len(nums1) and p2<len(nums2)):
            nums[i:len(nums)]=nums2[p2:len(nums2)]
            break
        elif(p2==len(nums2) and p1<len(nums1)):
            nums[i:len(nums)]=nums1[p1:len(nums1)]
            break
        else:
            if(nums1[p1]>nums2[p2]):
                nums[i]=nums2[p2]
                p2+=1
            else:
                nums[i]=nums1[p1]
                p1+=1
        i+=1
    return nums

if __name__=="__main__":
    # nums1=[0,1,-1,10,9,5,8,9,6,1]
    # nums2=[10]
    # nums3=[]
    # print(func_loop(nums1))
    # print(func_loop(nums2))
    # print(func_loop(nums3))
    nums1=[0,1,-1,10,9,5,8,9,6,1]
    nums2=[10]
    nums3=[]
    print(func_recrusion(nums1))
    print(func_recrusion(nums2))
    print(func_recrusion(nums3))