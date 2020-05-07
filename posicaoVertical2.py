import math
#
# Calcula quanto tempo a bola leva para atingir o solo após ser lançada para cima.
#

vi = float(input("Digite a velocidade inicial da bola: "))
y = float(input("Digite a posição desejada: "))

g = 9.81

a = g / 2
b = - vi
c = y

delta = b * b - 4 * a * c

if delta >= 0:
    if delta == 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        print("Apenas no tempo:", x1)

    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print("tempos: ", x2, x1)

else:
    print("Não atinge esta altura")
print("Fim")



