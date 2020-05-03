#
# Calcula a altura de uma bola lancada de uma torre em determinado instante de tempo
#
h = float(input("Digite a altura da torre em metros: "))
t = float(input("Digite o instante de tempo desejado em segundos: "))
g = 9.81

# Calcula o deslocamento a partir do repouso
s = g * (t**2/2)

# A altura da bola é igual a altura da torre menos o deslocamento
a = h - s
print("A altura da bola em relação ao solo é de:", a, "m")
