def binaryRepresentor(n):
    binaryList = []
    while n != 0:
        if n%2 == 0:
            binaryList.append(0)
            n = n//2 
        else:
            binaryList.append(1)
            n = n//2 
    temp = list(reversed(binaryList))
    return temp
