class Node:
    def __init__(self,city=None,plate=None,next=None):
            self.city=city
            self.plate=plate
            self.next=next

class Table:
   liste = []
   def __init__(self):
        for j in range(7):
            self.liste.append(Node("-1","-1"))
   

def readTextTableInit():
    global table1
    with open('/Users/ibrahimdagci/Desktop/python/AlgorithmsHomework1/data.txt', 'r') as f:
        lines = f.readlines()
    i = 0
    for line in lines:
        words = line.split()
        for word in words:
             if word != "->":
                wparts = word.split("/")
                if table1.liste[i].city == "-1":
                    table1.liste[i].city = wparts[0]
                    table1.liste[i].plate = wparts[1]
                else:         
                    temp = table1.liste[i]
                    while temp.next!=None:
                        temp  = temp.next
                    temp.next = Node("-1","-1")
                    temp.next.city = wparts[0]
                    temp.next.plate = wparts[1]    
        i+=1
    f.close

def printContiguitiList():
    global table1
    for i in range(7):
        temp = table1.liste[i]
        while temp.next !=None:
            print(f"{temp.city}/{temp.plate}",end="->")
            temp = temp.next
        print(f"{temp.city}/{temp.plate}",end="")
        print("\n")

def findInOut(plate):
    global table1
    countIn = 0
    countOut = 0
    isHere=False
    for i in range(7):
        temp = table1.liste[i]
        if temp.plate==plate:
            isHere = True
            while temp.next!=None:
                temp = temp.next
                countOut+=1
        else:
            while temp.next!=None:
                if temp.next.plate == plate:
                    countIn+=1
                temp = temp.next
    if isHere:
         print(f"şehrin {countIn} girişi, {countOut} çıkışı vardır")
    else:
        print("The city is not found!")   

def findEdgeCount():
    global table1
    edgeCount=0
    for i in range(7):
        temp = table1.liste[i]
        while temp.next!=None:
            edgeCount+=1
            temp=temp.next
    print(f"kenar sayısı:{edgeCount}")  

def findDestinations(plate):
    global table1
    countIn = 0
    countOut = 0
    isHere=False
    for i in range(7):
        temp = table1.liste[i]
        if temp.plate==plate:
            isHere=True
            print(f"{temp.city} şehrinden şu şehirlere gidilebilir:")
            while temp.next!=None:
                temp = temp.next
                print(temp.city)
    if not(isHere):
        print("The city is not found!")

def findDestinationWays(plate):
    global table1
    isHere=False
    for i in range(7):
        temp = table1.liste[i]
        if temp.plate==plate:
            print(f"{temp.city} şehrine şu şehirlerden gidilebilir:")
    for i in range(7):
        temp = table1.liste[i]
        if temp.plate!=plate:
            while temp.next!=None:
                if temp.next.plate == plate:
                    print(table1.liste[i].city)
                temp = temp.next
        else:
             isHere=True
    if not(isHere):
        print("The city is not found!")        

def userMenu():
    print("1-> listele\n2-> kenar sayısı bul\n3-> şehir giriş çıkışı sayısını bul")
    print("4-> a şehrinden hangi şehirlere gidebilirim?\n5-> a şehrine hangi şehirlerden gidebilirim?\n6...n-> çıkış")
    while True:
        index=int(input("yapmak istediğiniz işlemi seçiniz:"))
        if index==1:
            printContiguitiList()
        elif index==2:
            findEdgeCount()
        elif index==3:
            dataPlate = str(input("plaka girin:"))
            findInOut(dataPlate)
        elif index==4:
            dataPlate = str(input("plaka girin:"))
            findDestinations(dataPlate)
        elif index==5:
            dataPlate = str(input("plaka girin:"))
            findDestinationWays(dataPlate)
        else:
            break

table1 = Table()
readTextTableInit()
userMenu()