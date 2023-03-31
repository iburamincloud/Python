def gcd(num1, num2):
    global listDividing
    global listDivider
    global listDivision
    global listRemainder
    while num2 != 0:
        listDividing.append(num1)
        listDivider.append(num2)
        listDivision.append(num1//num2)
        listRemainder.append(num1%num2)
        num1, num2 = num2, num1 % num2

    return num1

def deleteEndIndex():
    global listDividing
    global listDivider
    global listDivision
    global listRemainder
    listDividing.pop()
    listDivider.pop()
    listDivision.pop()
    listRemainder.pop()
# this lists -> for loging and control
listDividing=[]
listDivider=[]
listDivision=[]
listRemainder=[]
#get user input
Temp=0
num1 = int(input("sayıyı girin: "))
num2 = int(input("sayıyı girin: "))
a = -1 #loop controller
b = 0  #loop controller
counterR=0  # x
counterL=0  # y
#change -> <-
if num1<num2:
    temp = num1
    num1 = num2
    num2 = temp

#main function
print("EBOB:", gcd(num1, num2))
if len(listDivision)>1:
    counterR=listDivision[-2]
    counterL=1
else:
    counterL = 1
    counterR = num1/num2 -1
deleteEndIndex()
for ab in listDivision:
    print(f"{listRemainder[a]} = {listDividing[a]} - {listDivider[a]}x{listDivision[a]}")
    if b>0:
        temp = counterR
        counterR = temp*listDivision[a] + counterL
        counterL = temp
    
    a-=1
    b+=1
#coefficients
print(counterL)
print(counterR)

#coefficient sign detection
if gcd(num1,num2)==num1*counterL+num2*counterR:
    print(f"ebob({num1},{num2}) = {num1}x{counterL} + {num2} x {counterR} = {gcd(num1,num2)}")
elif gcd(num1,num2)==num1*-counterL+num2*counterR:
    print(f"ebob({num1},{num2}) = {num1}x{-counterL} + {num2} x {counterR} = {gcd(num1,num2)}")
elif gcd(num1,num2)==num1*counterL+num2*-counterR:
    print(f"ebob({num1},{num2}) = {num1}x{counterL} + {num2} x {-counterR} = {gcd(num1,num2)}")
elif gcd(num1,num2)==num1*counterR+num2*counterL:
    print(f"ebob({num1},{num2}) = {num1} x {counterR} + {num2} x {counterL} = {gcd(num1,num2)}")
elif gcd(num1,num2)==num1*-counterR+num2*counterL:
    print(f"ebob({num1},{num2}) = {num1} x {-counterR} + {num2} x 1{counterL} = {gcd(num1,num2)}")
elif gcd(num1,num2)==num1*counterR+num2*-counterL:
    print(f"ebob({num1},{num2}) = {num1} x {counterR} + {num2} x {-counterL} = {gcd(num1,num2)}")
