import itertools
x=input("password possibilities?")
y=0
z=0
list(x)
k=list()
isim=input("what is the name of the file?")
isim=isim+".txt"
f = open(isim, "w")
for i in x:
    y = y + 1
    if i == "/" and z == 0:
        t = str(x[0:y - 1])
        k.append(t)
    if i == "/" and z != 0:
        k.append(str(x[z:y - 1]))
    if i == "/":
        z = y
print(k)
for n in range(1,len(k)+1):
    for xs in itertools.permutations(k,n):
        chars="".join(xs)
        if len(chars)<20 and len(chars)>5:
            print(chars)
            f.write(chars+"\n")
f.close()