def isPrime(n):
    result = False
    count = 0
    for i in range(1,n//2):
        if n%i == 0:
            count +=1
    if count < 2:
        result = True
    return result
