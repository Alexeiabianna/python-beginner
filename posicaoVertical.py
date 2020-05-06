#
# Calcula a posição de uma bola jogada para cima em um determinado instante de tempo.
#

vi = float(input("Digite a velocidade inicial da bola: "))
it = float(input("Digite um instante de tempo em segundos: "))

g = 9.81

y = vi * it - ((g * it**2) / 2)

print("A posição vertical da bola é: ", y, "m")