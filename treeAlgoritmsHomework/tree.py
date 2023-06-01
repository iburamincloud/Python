class Node:
    def __init__(self,data=None,leftLink=None,rightLink=None):
            self.data = data
            self.leftLink = leftLink
            self.rightLink = rightLink

dataList = [40,70,50,30,25,75,65,5,27,12,7,4,13,88]
root = None


def treeInit():
    global root
    temp = None
    for data in dataList:
        if root == None:
            root = Node(data)
        else:
            temp = root
            while temp != None:
                if data <= temp.data:
                    if temp.leftLink == None:
                         temp.leftLink = Node(data)
                         break
                    temp = temp.leftLink
                elif data > temp.data:
                    if temp.rightLink == None:
                         temp.rightLink = Node(data)
                         break
                    temp = temp.rightLink

def treeInitMirror():
    global root
    temp = None
    for data in dataList:
        if root == None:
            root = Node(data)
        else:
            temp = root
            while temp != None:
                if data >= temp.data:
                    if temp.leftLink == None:
                         temp.leftLink = Node(data)
                         break
                    temp = temp.leftLink
                elif data < temp.data:
                    if temp.rightLink == None:
                         temp.rightLink = Node(data)
                         break
                    temp = temp.rightLink
            
rankList = []    
def logRank(rank,parent):
    global rankList
    if len(rankList)<rank:
             rankList.append([])
    if parent != None:
        rankList[rank-1].append(parent.data)
        logRank(rank+1,parent.leftLink)
        logRank(rank+1,parent.rightLink)
    else:
        rankList[rank-1].append("null")
    
    

def printRankList():
    global rankList
    global root
    logRank(1,root)
    for i in range(len(rankList)-1):
        print(f"lvl {i+1} -> {rankList[i]}")
    rankList = []
    root = None
    
          
        
            

treeInit()
print("Mertebeler:") 
printRankList()
print("Simetriği alındıktan sonraki mertebeler:")
treeInitMirror()
printRankList()

            