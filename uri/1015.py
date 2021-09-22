from math import sqrt

x1, y1 = input().split()
x2, y2 = input().split()

dis = sqrt((float(x2)-float(x1))**2 + ((float(y2)-float(y1))**2))
print(f"{dis:.4f}")
