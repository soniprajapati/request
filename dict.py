a=int(input("enter"))
b={}
i=1
while i<=a:
    j=0
    d=[]
    while j<=10:
        sum=i*j
        d.append(sum)
        j+=1
    b.update({i:d})
    i+=1
print(b)
    