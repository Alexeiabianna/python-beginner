import math
#
# Cálculo da altura (h) para que um satélite atinga uma órbita geoestacionária.
#

T = float(input("Digite o tempo de órbita: "))
T = T * 60

G = 6.67428e-11
M = 5.97e24
R = 6371e3
pi = math.pi

h = ((G * M * T**2) / (4 * pi ** 2)) ** (1/3) - R




print(R)
print("A altitude que deverá estar o satélite para entrar em órbita circular é de: ", h)
