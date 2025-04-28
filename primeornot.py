N = int(input())

def isprime(num):
    for i in range(2, num//2):
        if(num%i == 0):
            return False
    return True

if(isprime(N) == True):
    print("Number is Prime")
else:
    print("Number is not Prime")