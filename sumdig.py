n=[45,73,105,7,54,80]
l=[]
for i in n:
    s=0
    for j in str(i):
        s=s+int(j)
    l.append(s)
print(l)