# №5
def p(x):
    return x>1 and all(x%i!=0 for i in range(2,int(x**0.5)+1))
primes = []
n = int(input())
for i in range(2,n):
    if p(i):
        primes += [i]
print(primes)
#почти как надо
