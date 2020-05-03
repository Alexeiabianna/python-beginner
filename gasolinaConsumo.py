km = float(input("Digite a distância percorrida em Km:"))
gas = float(input("Digite o consumo em litros gastos pelo veículo:"))

c = km / gas

print("O consumo médio do veículo é de", c, "Km/l")

cm = float(input("Digite a autonomia do veículo em Km/l: "))

gt = km / cm

print("O veículo deveria consumir o total de", gt, "litros ao percorrer a distância de", km, "Km")
