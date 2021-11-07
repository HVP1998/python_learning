import func_ExchangeTwoNumbers

def func(nums):
    for i in range(0,len(nums)-1):
        for j in range(0,len(nums)-1-i):
            if(nums[j]>nums[j+1]):
                nums[j],nums[j+1]=func_ExchangeTwoNumbers.func(nums[j],nums[j+1])