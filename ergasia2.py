
primeNumbers=[]
for i in range(2,1000):
    count=0
    for j in range(2,i+1):
        if i%j==0:
            count=count+1
    if count==1:
        primeNumbers.append(i)
print(primeNumbers)
number=int(input("Arithmos gia paragontopoihsh: "))
x=[]
pos=0
while number > 1:
    if number%primeNumbers[pos]==0:
        x.append(primeNumbers[pos])
        number=number/primeNumbers[pos]
    else:
        pos=pos+1
length=len(x)
pos2=[0]
for i in range(length-1):
    if x[i]!=x[i+1]:
        pos2.append(i+1)
times=[]
for i in (pos2):
    times.append(x.count(x[i]))
y=[]
for i in pos2:
    y.append(x[i])
for i in range(len(y)):
    print("(",y[i],"**",times[i],end=")")
