#! /usr/local/bin/python3
# _*_ coding:utf-8 _*_
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left ,self.right= None ,None

def searchRange(root,k1,k2):
    if root.val >= k1 and root.val <= k2:
        yield root.val 
    if root.left != None:
        yield from searchRange(root.left,k1,k2)
    if root.right != None:
        yield from searchRange(root.right,k1,k2)
    

#{3,9,20,#,#,15,7}
"""
  3
 / \
9  20
   /  \
  15   7
"""
def createTree(root):
    if root[0] == "#" or root == []:
        return None
    else:
        root = TreeNode(int(root[0]))
    for i in root[1:]:
        if i=="#":
            return None
        else:
            return TreeNode(int(i))


def levelOrder(root):
     
    for i in root:
        


if __name__ == "__main__":
    floor=TreeNode(20)
    floor11=TreeNode(8)
    floor12=TreeNode(22)
    floor21=TreeNode(4)
    floor22=TreeNode(12)
    floor.left=floor11
    floor.right=floor12
    floor11.left=floor21
    floor11.right=floor22
    
    root = TreeNode(18)
    rootright=TreeNode(9)
    root.left=floor
    root.right=rootright

    #print(floor.left.left)
    result=[]
    for i in searchRange(root,10,22):
        result.append(i)
    
    print(sorted(result))
    o
