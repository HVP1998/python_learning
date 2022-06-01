def GetVar(nums,avg):
    var=0.0
    for num in nums:
        var=var+pow(num-avg,2)/len(nums)
    return var