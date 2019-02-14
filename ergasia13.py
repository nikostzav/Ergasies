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
    print(sum,x)
maxDistance([1,5,2,7,3,5],15) #output

