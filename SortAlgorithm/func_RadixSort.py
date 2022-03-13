def RadixSort(nums):
    zero=0
    max_length=len(nums[0])
    # 取得最大长度
    for i in range(1,len(nums),1):
        if(len(nums[i])>max_length):
            max_length=len(nums[i])
    # 给列表补零
    for i in range(0,len(nums),1):
        if(len(nums[i])<max_length):
            zero=max_length-len(nums[i])
            nums[i]=zero*"0"+nums[i]

    for i in range(max_length-1,-1,-1):
        for j in range(0,len(nums)-1,1):
            for k in range(0,len(nums)-1-j,1):
                if(int(nums[k][i])>int(nums[k+1][i])):
                    num_new=nums[k]
                    nums[k]=nums[k+1]
                    nums[k+1]=num_new
    if(zero==0):
        return
    for i in range(0,len(nums),1):
        num_new=nums[i][0:zero]
        if(num_new==zero*"0"):
            nums[i]=nums[i][zero:len(nums[i])]
            print()
            

    
    
        



if __name__=="__main__":
    # nums=[6,4,7,3,2,11,10,5,9,1,8]
    nums=[76,85,84,79,80,82,80,79,78,78]
    for i in range(0,len(nums),1):
        nums[i]=str(nums[i])
    RadixSort(nums)
    for i in range(0,len(nums),1):
        nums[i]=int(nums[i])
    print(nums)