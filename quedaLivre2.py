import math
#
# Calcula a altura de uma bola lancada de uma torre em determinado instante de tempo
#
h = float(input("Digite a altura da torre: "))
g = 9.81
t = math.sqrt((2 * h)/g)

print("O tempo para a bola tocar o solo é de: ", t, "segundos")
