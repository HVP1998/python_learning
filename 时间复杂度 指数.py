def algorithm(N):
    if N<=0:return 1
    count_1=algorithm(N-1)
    print("count_1======>%d"%count_1)
    count_2=algorithm(N-1)
    print("count_2======>%d"%count_2)
    return count_1+count_2