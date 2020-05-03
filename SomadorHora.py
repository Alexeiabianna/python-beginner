# Programa simples para estudo de variáveis

horaAtual = int(input("Digite a hora atual: "))
wait = int(input("Quantas horas você quer esperar? "))

horas = horaAtual + wait

horaDoDia = horas % 24

print("O alarme irá tocar as", horaDoDia, ":00 horas")