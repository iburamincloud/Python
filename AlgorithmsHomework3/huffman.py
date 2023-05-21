class Node:
    def __init__(self,char=None,count=None,leftLink=None,rightLink=None):
            self.char=char
            self.count=count
            self.leftLink=leftLink
            self.rightLink=rightLink

mesaj = ""
charList = []
charNodes = []
charCodes = {}

def removeNodes():
    global mesaj
    global charList
    global charNodes 
    global charCodes 
    mesaj = ""
    charList = []
    charNodes = []
    charCodes = {}


def userMenu():
    while True:
        print("menu")
        print("1-> mesaj sıkıştır.\n2-> mesaj aç\n3-> çıkış")
        answ = input("lütfen seçiminizi giriniz: ")
        if answ == "1":
            removeNodes()
            getMessage()
            readdNodeC()
            for i in charNodes:
                print(i.char,end="->")
                print(i.count)
            print("----------")
            mergeNodes()
            preorderVisit(charNodes[0],"")
            listCharCodeCD()
            encoder()
        elif answ == "2":
            getMessage()
            decoder()
        elif answ == "3":
            break
        else:
            print;("hatalı tuşlama yaptınız tekrar deneyin!!!")

#mesaj alınır.
def getMessage():
    global mesaj
    mesaj = input("Lütfen mesajınızı giriniz: ")

#alınan mesaj karakter karakter okunur ve her farklı karakter için bir düğm oluşturulup düğümler listesine eklenir.
#aynı karakter okunursa düğümdeki counter 1  artırılır.
def readdNodeC():
    for i in mesaj:
        if not(i in charList):
            charNodes.append(Node(i,1))
            charList.append(i)
        else:
            for j in charNodes:
                if i == j.char:
                    j.count+=1

#düğümleri frekanslarına göre sıralar küçükten büyüğe
def sortNodes():
    tempNodes = []
    for i in range(len(charNodes)):
        for j in range(len(charNodes)-1):
            if charNodes[j].count >= charNodes[j+1].count:
                temp = charNodes[j+1]
                charNodes[j+1] = charNodes[j]
                charNodes[j] = temp


#düğümleri frekanslara göre birleştirme en küçük frekanslı iki düğüm ilk başta birleştirilip tek bir düğüm haline getirilir.(ağacı oluşturma)
def mergeNodes():
    temp1 = None
    temp2 = None
    if len(charNodes)> 1:
        sortNodes()
        temp1  = charNodes[0]
        temp2 = charNodes[1]
        charNodes.append(Node("",temp1.count+temp2.count,temp1,temp2))
        charNodes.remove(temp1)
        charNodes.remove(temp2)
        for i in charNodes:
            print(i.char,end="->")
            print(i.count)
        print("----------")
        mergeNodes()
    else:
        print("ağaç oluşturuldu.")
        
#ağacı preorder dolaşıp karakter kodlarını bulma ve listeye atama 
def preorderVisit(node,code):
    if node.char == "":
        preorderVisit(node.leftLink,code + "0")
        preorderVisit(node.rightLink,code + "1")
    else:
        charCodes[node.char] = code


#karakter kodlarını ekrana bastırma
def listCharCodeCD():
    print("karakter kodları:",end="->")
    print(charCodes)


#mesajı kod listesine göre kodlama
def encoder():
    print("kodlanmış mesaj:")
    code = ""
    for char in mesaj:
        code = code + charCodes[char]
    print(code)
    # sıkıştırma yüzdesi hesabı((orjinalmesaj boyutu - sıkışmış mesaj boyutu)/orjinal boyut *100)
    print(f"sıkıştırma yüzdesi = %{((len(mesaj)*8)-len(code))/(len(mesaj)*8)*100}")

def decoder():
    tempNode = charNodes[0]
    message = ""
    for i in mesaj:
        if i=="0":
            if tempNode == None:
                message = "bu mesaj açmılmak için uygun deği!!!!"
                break 
            else:
               tempNode = tempNode.leftLink
        elif i=="1":
            if tempNode == None:
                message = "bu mesaj açmılmak için uygun deği!!!!"
                break
            else:
                tempNode = tempNode.rightLink
        else:
            message = "bu mesaj açmılmak için uygun deği!!!!"
            break
        if tempNode == None:
            message = "bu mesaj açmılmak için uygun deği!!!!"
            break
        if tempNode.char!="":
            message = message + tempNode.char
            tempNode = charNodes[0]
    if tempNode != charNodes[0]:
        print("fazladan binary karakter saptandı!!!")
        message = message + "????"
    print(message)
        

userMenu()