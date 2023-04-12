max_row = 0
max_column = 0
matris = []
color = []
pred = []
findedIn= []
blackedIn = []

def readGraph():
    global matris
    global max_column
    global max_row
    with open('/Users/ibrahimdagci/Desktop/python/AlgorithmsHomework2/graph.txt','r') as g:
        lines = g.readlines()
        max_column = max_row= len(lines)
        g.close
        
    defaultInit()
    i=0
    for line in lines:
        chars = line.split(" ")
        j=0
        for char in chars:
            matris[i][j]=int(char)
            j+=1
        i+=1
            
def defaultInit():
    global matris
    global color
    global pred
    global findedIn
    global blackedIn
    global max_row
    global max_column
    for i in range(max_row):
        row = []
        color.append(0)
        pred.append(-1)
        findedIn.append(-1)
        blackedIn.append(-1)
        for j in range(max_column):
            row.append(0)
        matris.append(row)

def listNeighbour():
    print("komşuluk listesi:")
    global matris
    global max_row
    rowNum = 0
    for i in range(max_row):
        print(f"{rowNum}:",end= " ")
        index = 0
        for j in matris[i]:
            if j== 1:
                print(index,end=" ")
            index+=1
        rowNum+=1
        print()
    print()


def DFS():
    global max_row
    time = 0
    for i in range(max_row):
        if color[i]==0:
            DFSVisit(i,time)

def DFSVisit(i,time):
    color[i] = 1
    time+=1
    print(f"{i}. düğüm ziyaret edildi")
    findedIn[i]= time
    index = 0
    for j in matris[i]:
        if j==1:
            if color[index]==0:
                DFSVisit(index,time)
        index+=1
    color[i]=2
    print(f"{i}. düğüm siyaha çevrildi")
    time+=1
    blackedIn[i]=time


readGraph()
listNeighbour()
DFS()