def GetAvg(nums):
    avg=0.0
    for num in nums:
        avg=avg+num/len(nums)
    return avg