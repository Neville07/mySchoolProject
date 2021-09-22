import math
a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

mab = (a + b + abs(a - b))/2
mf = (mab + c + (abs(mab - c)))/2
print(f"{int(mf)} eh o maior")
