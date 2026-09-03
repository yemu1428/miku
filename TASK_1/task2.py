import time
a=[["A",1,2],["B",2,0],["C",0,1]]
p=0
while True:
    b=int(input())
    if b==1:
        p=a[p][1]
    elif b==2:
        p=a[p][2]
    s=time.strftime("%Y-%m-%d %H:%M:%S")
    print(s,a[p][0])