i=0

while i < 6:
    print(i)
    i +=1
print("---Break------")
j=0
while j < 6:
    print(j)
    j +=1
    if j ==3:
        break
print("---Continue-------")
k=0
while k < 6:
    k += 1
    if k ==3:
        continue
    print(k)
print("---Else----")
a=0
b=10
while a<b:
    print(a)
    a += 1
else: # once loop break, it executes else
    print('A is no more greater than %d'%(b))