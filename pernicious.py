#a number which it's binary representation is prime for instance 5 binary is 101 so add them we get 3 so 3 is prime 

def isPrime(n):
    result = False
    count = 0
    for i in range(1,n//2+1):
        if n%i == 0:
            count +=1
    if count < 2:
        result = True
    return result
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
count = 0
for i in range(222281, 222381):
    count = 0
    temp = binaryRepresentor(i)
    for j in temp:
        if j == 1:
            count+=1
    if isPrime(count):
        print(i)


                
