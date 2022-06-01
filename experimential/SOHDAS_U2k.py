# 将MATLAB中公式中的关于U的矩阵计算转变为关于k的矩阵计算
def t2U(equ:str)->str:
    res=list()
    for i in range(0,len(equ)):
        if(equ[i]=='k'):
            if(equ[i+1]=="^"):
                res.append(equ[i])
                res.append('.')
            else:
                res.append(equ[i])
        elif(equ[i]=="."):
            pass
        else:
            res.append(equ[i])
    return "".join(res)


    
equ="-(U.^12*beta^11*k^12/685765402243891200)*(k^9*(x^10)*30349541376+k^7*(x^8)*502196808960-k^5*(x^6)*993841242240-k^3*(x^4)*7696444371000-k*(x^2)*1310910158250)"
res=t2U(equ)
print(res)