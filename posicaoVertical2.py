import math
#
# Calcula quanto tempo a bola leva para atingir o solo após ser lançada para cima.
#

vi = float(input("Digite a velocidade inicial da bola: "))

g = 9.81
y = 0
t = math.sqrt(vi * y * g * 2) # Falta resolver isso para quinta


print("O tempo para a bola tocar o solo é de: ", t, "m")