'''




'''
def func_loop(nums:list,num:int)->list:
    if(len(nums)<=1):return nums
    bucket,nums_new=list(),[]
    for i in range(0,num):
        bucket.append([])
    min=max=nums[0]
    for i in range(1,len(nums)):
        if(min>nums[i]):min=nums[i]
        elif(max<nums[i]):max=nums[i]
    step=(max-min)/num
    for i in range(0,len(nums)):
        if(nums[i]==max):
            bucket[num-1].append(nums[i])
            continue
        d=int((nums[i]-min)/step)
        bucket[d].append(nums[i])
    for i in range(0,len(bucket)):
        for j in range(0,len(bucket[i])-1):
            for k in range(0,len(bucket[i])-1-j):
                if(bucket[i][k]>bucket[i][k+1]):
                    bucket[i][k]=bucket[i][k]+bucket[i][k+1]
                    bucket[i][k+1]=bucket[i][k]-bucket[i][k+1]
                    bucket[i][k]=bucket[i][k]-bucket[i][k+1]
        nums_new=nums_new+bucket[i]
    return nums_new

# def func_recrusion(nums:list)->list:
#     if(len(nums)<=1):return nums
#     nums[0:int(len(nums)/2)]=func_recrusion(nums[0:int(len(nums)/2)])
#     nums[int(len(nums)/2):len(nums)]=func_recrusion(nums[int(len(nums)/2):len(nums)])
#     nums1=nums[0:int(len(nums)/2)]
#     nums2=nums[int(len(nums)/2):len(nums)]
#     p1,p2,i=0,0,0
#     while(True):
#         if(p1==len(nums1) and p2==len(nums2)):
#             break
#         elif(p1==len(nums1) and p2<len(nums2)):
#             nums[i:len(nums)]=nums2[p2:len(nums2)]
#             break
#         elif(p2==len(nums2) and p1<len(nums1)):
#             nums[i:len(nums)]=nums1[p1:len(nums1)]
#             break
#         else:
#             if(nums1[p1]>nums2[p2]):
#                 nums[i]=nums2[p2]
#                 p2+=1
#             else:
#                 nums[i]=nums1[p1]
#                 p1+=1
#         i+=1
#     return nums

if __name__=="__main__":
    nums1=[0,1,-1,10,9,5,8,9,6,1]
    nums2=[10]
    nums3=[]
    print(func_loop(nums1,5))
    print(func_loop(nums2,5))
    print(func_loop(nums3,5))
    # nums1=[0,1,-1,10,9,5,8,9,6,1]
    # nums2=[10]
    # nums3=[]
    # print(func_recrusion(nums1))
    # print(func_recrusion(nums2))
    # print(func_recrusion(nums3))