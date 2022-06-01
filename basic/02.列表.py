
#*********************************列表*********************************
# list=[None]*5
# print(list)
# str="*555A"*3
# print(str)



"""增"""
# append整体添加
# langage=["Chinese","English","Japanese"]
# year=[1998,1999,2000]
# new_list=langage+year
# print(new_list)
# new_list.append(["none",25,36.6])
# print(new_list)
# new_list.append(("JavaScript",".Net","H5C3"))
# print(new_list)

# extend逐个添加
# code=["C#","Python","Java"]
# print(code)
# code.extend(["JavaScript","html","css"])
# print(code)
# code.extend(("C++","C","PHP"))
# print(code)

# insert插入
# code=["C#","Python","Java"]
# print(code)
# code.insert(1,["JavaScript","html","css"])
# print(code)
# code.insert(0,("C++","C","PHP"))
# print(code)

"""删"""
# language1=list(["python","Java","C#","C++","JS","matlab"])
# del language1[5]
# print(language1)
# language2=list(["python","Java","C#","C++","JS","matlab"])
# language2.pop(5)
# print(language2)
# language3=list(["python","Java","C#","C++","JS","matlab"])
# language3.remove("matlab")
# print(language3)
# language4=list(["python","Java","C#","C++","JS","matlab"])
# del language4[2:3]
# print(language4)
# language5=list(["python","Java","C#","C++","JS","matlab"])
# language5.clear()
# print(language5)

"""改"""
# monster=["梼杌","混沌","穷奇","饕餮"]
# # 切片时不允许插入单独数据
# monster[3:3]=["傲狠","帝江","狍鸮"]
# print(monster)
# monster[0:7:2]=["1","3","4","6"]
# print(monster)

"""查"""
# son_of_dragon=["囚牛","睚眦","嘲风","蒲牢","狻猊","赑屃","狴犴","负屃","鸱吻"]
# print(son_of_dragon.index("鸱吻"))
# print(son_of_dragon.count("螭吻"))

# a=["what kind of ways do you want to olden",28,("The greatest normality should be cherished",),("Do I will expect tomorrow?")]
# print(type(a))
# print(type(a[2]))
# print(type(a[3]))
# b=23,a,"may be there are something else"
# print(type(b))
# c=(3.14159265,"F2",'3',5,["time is going by"])
# print(type(c))
# d=tuple(a)
# print(type(d))
# print(d)
#**********************************************************************



#*******************************字典*************************************
"""创建字典"""
# a={"love":2.5,"leave":3.5,"dream":2.5,"reality":3.5}
# print(type(a))
# str=["find","home","girl","truth","fairy"]
# b=dict.fromkeys(str,None)
# print(type(b))
# c=dict(Iseeyouagain=1,fromnorthtosouth=2,Iwantdrinkagain=3,theAutumn=4)
# print(type(c))
# d1=([1,1],[2,2],[3,3])
# d1=dict(d1)
# d2=((1,1),(2,2),(3,3))
# d2=dict(d2)
# d3=[[1,1],[2,2],[3,3]]
# d3=dict(d3)
# d4=[(1,1),(2,2),(3,3)]
# d4=dict(d4)
# print("d1:",type(d1),end="")
# print("\td2:",type(d2),end="")
# print("\td3:",type(d3),end="")
# print("\td4:",type(d4))
# keys=("一乡","共三夫子","五经","竟敢教七","九子")
# values=("二里","不识四书","六艺","八","十分大胆")
# e=dict(zip(keys,values))
# print(e)
"""访问字典"""
# a={"dream":False,"reality":True}
# print(a.get("dream","不存在"))
# print(a.get("truth","不存在"))
"""增"""
# a={"七绝圣手":"王昌龄"}
# a["易安居士"]="李清照"
# a["青莲居士"]="杜甫"
# a["五柳先生"]="柳宗元"
# print(a)
"""改"""
# a["青莲居士"]="李白"
# print(a)
"""删"""
# del a["易安居士"]
# print(a)
# a.pop("七绝圣手")
# print(a)
# a.popitem()
# print(a)
"""查"""
# print("青莲居士" in a)
#**********************************************************************



#**********************************集合**********************************
"""创建set集合"""
# a={1,"2",'3',3.14,True}
# print("a------->",type(a),"===",a)
# b=set({1:1,2:2,3:3})
# print("b------->",type(b),"===",b)
# c=set((3.14,(1,2,3),"S"))
# print("c------->",type(c),"===",c)
# d=set(["A","B",'C',2.35,2])
# print("d------->",type(d),"===",d)
"""访问set集合元素"""
# a={1,2,3,4,5}
# for i in a:
#     print(i,"\t",end="")
"""删除set集合"""
# a={1,2,3,4,5}
# del a
"""set集合增加元素、更新、并、交..."""
# a={1,2,3,6}
# b={3,4,5,6}
# a.add((1,2))
# print("给a增加元素:",a)
# a.update(b)
# print("将b集合更新给a:",a)
# a={1,2,3,6}
# b={3,4,5,6}
# c=a.difference(b)
# print("将a中a与b重合的元素删除给c:",c)
# a.difference_update(b)
# print("将a中a与b重合的元素删除更新给a:",a)
# a={1,2,3,6}
# b={3,4,5,6}
# c=a.symmetric_difference(b)
# print("将a与b中a与b重合的元素删除后取a与b的交给c:",c)
# a.symmetric_difference_update(b)
# print("将a与b中a与b重合的元素删除后取a与b的交更新给a:",a)
# a={1,2,3,6}
# b={3,4,5,6}
# c=a.intersection(b)
# print("将a与b的交给c:",c)
# a.intersection_update(b)
# print("将a与b的交更新给a:",a)
# a={1,2,3,6}
# b={3,4,5,6}
# c=a.union(b)
# print("将a与b的并给c:",c)
# a={1,2,3,6}
# b={3,4,5,6}
# a.remove(3)
# b.discard(6)
# print("将a中的元素删除:",a)
# print("将b中的元素删除:",b)
# c=a.pop()
# print("将a中的元素取一个给c:",c)
# a.clear()
# print("空集：",a)
# a={1,2,3,6}
# b={3,4,5,6}
# print("判断a与b是否有交:",a.isdisjoint(b))
# print("判断a是否为b的子集:",a.issubset(b))
# print("判断a是否为b的父集:",a.issuperset(b))
# """创建frozenset集合"""
# a=frozenset(["2.5","Java"])
# print("a======>",type(a))