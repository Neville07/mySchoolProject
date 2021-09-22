c1 = input().split(" ")
c2 = input().split(" ")

code1, pro1, num1 = c1
code2, pro2, num2 = c2 

total = (int(pro1) * float(num1) + (int(pro2) * float(num2)))
print(f"VALOR A PAGAR: R$ {total:.2f}")
