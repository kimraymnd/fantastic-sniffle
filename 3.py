import math
# x = 2
n = input("Enter a number: ")

n = int(n)

def isPrime(n):
    for x in range(2, int(math.sqrt(n))+1):
        if (n%x==0):
            return False
    return True

print(isPrime(n))
