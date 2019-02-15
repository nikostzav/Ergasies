def maxDistance(numbs,max):
    pos=0
    sum=0
    x=[]
    for i in range(len(numbs)):
        if sum+numbs[pos]<=max:
            sum+=numbs[pos]
            x.append(numbs[pos])
            pos+=1
        else:
            pos+=1
    return sum
print(maxDistance([2,6,4,7,3],8)) #<-- output

