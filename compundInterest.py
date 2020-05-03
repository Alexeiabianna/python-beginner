p = float(input("Digite o valor do investimento inicial: "))
r = 0.08
n = 12
t = int(input("Digite o número de anos do investimento: "))

p = (float(p))
t = (int(t))

a = p * (1 + r/n) ** (n*t)

print("O resultado final depois de", t, "anos é", a)