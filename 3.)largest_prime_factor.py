import math
def prime(num):
        for i in range(2, num):
            if (num % i) == 0:
                return False
        else:
            return True

for i in range(int(math.sqrt(600851475143)), 2, -1):
    if 600851475143%i == 0 and prime(i):
        print(i)

#ans = 6857
