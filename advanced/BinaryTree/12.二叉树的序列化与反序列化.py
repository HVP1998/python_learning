# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root:TreeNode):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if(not root):return "null"
        tmp=[str(root.val)]
        queue=[root]
        while(len(queue)):
            cur=queue.pop(0)
            if(cur.left):
                queue.append(cur.left)
                tmp.append(str(cur.left.val))
            else:
                tmp.append("null")
            if(cur.right):
                queue.append(cur.right)
                tmp.append(str(cur.right.val))
            else:
                tmp.append("null")
        res=(",".join(tmp)).strip(",null")
        return res
        
        


        

    def deserialize(self, data:str):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if(data=="null"):return None
        data_new=data.split(",")
        root=TreeNode(int(data_new.pop(0)))
        queue=[root]
        while(len(data_new)>0):
            cur=queue.pop(0)
            tmp=data_new.pop(0)
            if(tmp!="null"):
                cur.left=TreeNode(int(tmp))
                queue.append(cur.left)
            if(len(data_new)==0):break
            tmp=data_new.pop(0)
            if(tmp!="null"):
                cur.right=TreeNode(int(tmp))
                queue.append(cur.right)
        return root


if __name__=="__main__":
    node0=TreeNode(0)
    node1=TreeNode(1)
    node2=TreeNode(2)
    node0.left=node1
    node0.right=node2
    node3=TreeNode(3)
    node4=TreeNode(4)
    node5=TreeNode(5)
    node6=TreeNode(6)
    node1.left=node3
    node1.right=node4
    node2.left=node5
    node2.right=node6
    node7=TreeNode(7)
    node8=TreeNode(8)
    node9=TreeNode(9)
    node10=TreeNode(10)
    node11=TreeNode(11)
    node12=TreeNode(12)
    node13=TreeNode(13)
    node14=TreeNode(14)
    node3.left=node7
    node3.right=node8
    node4.left=node9
    node4.right=node10
    node5.left=node11
    node5.right=node12
    node6.left=node13
    node6.right=node14
    C=Codec()
    print(C.deserialize(C.serialize(node0)))