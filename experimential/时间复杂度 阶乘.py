def alg(N):
    if(N<=0):
        return 1
    num=0
    for i in range(N):
        num+=alg(N-1)
    return num