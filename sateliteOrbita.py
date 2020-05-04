#
# Cálculo da altura (h) para que um satélite atinga uma órbita geoestacionária.
#

T = float(input("Digite o tempo de órbita: "))

G = 6.67428 * 1e-11
M = 5.97 * 1e24
R = 6371 * 1000
pi = 3.14159

h = (((G * M * (T**2))/(4 * pi)**2)**(1/3)) - R


print(R)
print("A altitude que deverá estar o satélite para entrar em órbita circular é de: ", h)
