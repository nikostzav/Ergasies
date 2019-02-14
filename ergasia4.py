#Sunarthseis arithmwn
def one(*numb):
    if numb:

        if numb[0][0]=="+":
            print(1+int(numb[0][1]))
        elif numb[0][0]=="*":
            print(1*int(numb[0][1]))
        elif numb[0][0]=="-":
            print(1-int(numb[0][1]))
    else:
        return 1
def two(*numb):
    if numb:

        if numb[0][0]=="+":
            print(2+int(numb[0][1]))
        elif numb[0][0]=="*":
            print(2*int(numb[0][1]))
        elif numb[0][0]=="-":
            print(2-int(numb[0][1]))
    else:
        return 2
def three(*numb):
    if numb:

        if numb[0][0]=="+":
            print(3+int(numb[0][1]))
        elif numb[0][0]=="*":
            print(3*int(numb[0][1]))
        elif numb[0][0]=="-":
            print(3-int(numb[0][1]))
    else:
        return 3
def four(*numb):
    if numb:

        if numb[0][0]=="+":
            print(4+int(numb[0][1]))
        elif numb[0][0]=="*":
            print(4*int(numb[0][1]))
        elif numb[0][0]=="-":
            print(4-int(numb[0][1]))
    else:
        return 4
def five(*numb):
    if numb:

        if numb[0][0]=="+":
            print(5+int(numb[0][1]))
        elif numb[0][0]=="*":
            print(5*int(numb[0][1]))
        elif numb[0][0]=="-":
            print(5-int(numb[0][1]))
    else:
        return 5
def six(*numb):
    if numb:

        if numb[0][0]=="+":
            print(6+int(numb[0][1]))
        elif numb[0][0]=="*":
            print(6*int(numb[0][1]))
        elif numb[0][0]=="-":
            print(6-int(numb[0][1]))
    else:
        return 6
def seven(*numb):
    if numb:

        if numb[0][0]=="+":
            print(7+int(numb[0][1]))
        elif numb[0][0]=="*":
            print(7*int(numb[0][1]))
        elif numb[0][0]=="-":
            print(7-int(numb[0][1]))
    else:
        return 7
def eight(*numb):
    if numb:

        if numb[0][0]=="+":
            print(8+int(numb[0][1]))
        elif numb[0][0]=="*":
            print(8*int(numb[0][1]))
        elif numb[0][0]=="-":
            print(8-int(numb[0][1]))
    else:
        return 8
def nine(*numb):
    if numb:

        if numb[0][0]=="+":
            print(9+int(numb[0][1]))
        elif numb[0][0]=="*":
            print(9*int(numb[0][1]))
        elif numb[0][0]=="-":
            print(9-int(numb[0][1]))
    else:
        return 9
#Sunarthseis praksewn
def plus(numb):
    x=["+",str(numb)]
    return x
def times(numb):
    x=["*",str(numb)]
    return x
def minus(numb):
    x=["-",str(numb)]
    return x
five(times(four()))#    <-- Output
