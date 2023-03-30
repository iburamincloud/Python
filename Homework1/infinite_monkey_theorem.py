import random
import time

i = True
k=False
t=False
u=False
n=False
countert=0
counteru=0

def falseAssign():
    global countert
    global counteru
    global k
    global t
    global u
    global n
    countert=0
    counteru=0
    k=False
    t=False
    u=False
    n=False
    
    
started_time = time.time()
while i:
    char = random.randint(97,122)
    print(chr(char),end=" ")
    if chr(char)=="k":
        k = True
        if countert==1:
            falseAssign()
        continue
    elif chr(char)=="t" and k==True:
        if countert ==0:
            t = True
            countert+=1
            continue
        else:
            falseAssign()
    elif chr(char)=="u" and k==True and t==True:
        if counteru ==0:
            u = True
            counteru+=1
            continue
        else:
            falseAssign()
    elif chr(char)=="n" and k==True and t==True and u==True:
        n = True
        break
    else:
        falseAssign()

print("\n-> ktun found")
print("time:",end=" ")
print((time.time() - started_time),end=" ")
print("sn") 