'''
请实现两个函数，分别用来序列化和反序列化二叉树。
你需要设计一个算法来实现二叉树的序列化与反序列化。
不限定你的序列 / 反序列化算法执行逻辑。
需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
'''
"""

---------------------------------------------------------------------------
答案精进：优化从字符串到二叉树的转变：当前为null时不做任何操作即可，从而减少了空间、时间资源的占用
"""
# Definition for a binary tree node.
from posixpath import split
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 时间与空间资源占用过多
class Codec:
    def serialize(self, root):
        # 空树返回
        if(not root):return "null"
        # 数据初始化
        queue,res,tmp,i,pos=[root],[],[],0,0
        while(True):
            empty=True
            for _ in range(len(queue)):
                cur=queue.pop(0)
                if(not cur):
                    tmp.append("null")
                else:
                    queue.append(cur.left)
                    queue.append(cur.right)
                    tmp.append(str(cur.val))
                    empty,pos=False,i
                i+=1
            if(empty):break
            res.extend(tmp)
            tmp=[]
        res=(",".join(res[:pos+1]))
        return res
    def deserialize(self, data):
        if(data=="null"):return None
        tmp=data.split(',')
        queue=[TreeNode(tmp[0])]
        root,jump=queue[0],0
        for i in range(len(tmp)):
            cur=queue.pop(0)
            if(cur==None):
                jump+=2
                continue
            if(2*i+1-jump<len(tmp)):
                if(tmp[2*i+1-jump]=='null'):cur.left=None
                else:cur.left=TreeNode(tmp[2*i+1-jump])
                queue.append(cur.left)
            if(2*i+2-jump<len(tmp)):
                if(tmp[2*i+2-jump]=='null'):cur.right=None
                else:cur.right=TreeNode(tmp[2*i+2-jump])
                queue.append(cur.right)
        return root
# 答案精进：优化空间与时间复杂度
class Codec_answer:
    def serialize(self, root):
        if not root: return "[]"
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            node = queue.popleft()
            if node:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else: res.append("null")
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        if data == "[]": return
        vals, i = data[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root

if __name__=="__main__":    
    node1=TreeNode(1)
    node2=TreeNode(2)
    node3=TreeNode(3)
    node4=TreeNode(4)
    node6=TreeNode(6)
    node7=TreeNode(7)
    node9=TreeNode(9)
    node12=TreeNode(12)
    node13=TreeNode(13)
    node1.left=node2
    node1.right=node3
    node2.left=node4
    node3.left=node6
    node3.right=node7
    node4.right=node9
    node6.left=node12
    node6.right=node13
    C=Codec_answer()
    print(C.serialize(C.deserialize(C.serialize(node1))))