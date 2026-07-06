p = float(input("Enter principal: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))
amount = p * (1 + r / 100) ** t
ci = amount - p
print("Amount =", amount)
print("Compound Interest =", ci)