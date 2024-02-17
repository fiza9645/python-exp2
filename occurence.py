n=input("enter the word:")
s=""
r=""
for i in n:
    if i not in s:
        s=s+i
    elif i not in r:
        r=r+i
print("Reapting letter is",r)