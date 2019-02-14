numbers=[5,6,4,7,3,1]
max=int(input("Megistos arithmos: "))
pos=0
sum=0
x=[]
for i in range(len(numbers)):
    if sum+numbers[pos]<=max:
        sum+=numbers[pos]
        x.append(numbers[pos])
        pos+=1
    else:
        pos+=1
print(sum,x)
