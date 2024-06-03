
v = float(input("Digite o valor do depósito inicial: "))
d = float(input("Digite o valor dos depósitos mensais: "))
m = int(input("Digite a quantidade de meses: "))
j = float(input("Digite a taxa de juros: "))

def calcula_saldo(valor, deposito, mes, juros):

    valor = valor + (valor * juros)
    mes -= 1
    deposito_inicial = valor + deposito + (valor + deposito) * juros
    mes -= 1

    while mes != 0:
        deposito_inicial = deposito_inicial + deposito + (deposito_inicial + deposito) * juros
        mes -= 1
    if mes == 0:
        s = "%.2f" % round(deposito_inicial + d, 2)
        return s



def conta_notas():

    s = calcula_saldo(v, d, m, j)
    print(f"Após {m} meses, o saldo final foi de {s} reais.")
    print(f"Os {s} reais foram sacados com:")

    resto_100 = float(s) % 100
    notas_100 = (float(s) - resto_100) / 100
    print(f"{int(notas_100)} nota(s) de 100 reais")

    resto_50 = resto_100 % 50
    notas_50 = (resto_100 - resto_50) / 50
    print(f"{int(notas_50)} nota(s) de 50 reais")

    resto_10 = resto_50 % 10
    notas_10 = (resto_50 - resto_10) / 10
    print(f"{int(notas_10)} nota(s) de 10 reais")

    resto_2 = resto_10 % 2
    notas_2 = (resto_10 - resto_2) / 2
    print(f"{int(notas_2)} nota(s) de 2 reais")

    resto_1 = resto_2 % 1
    moedas_1 = (resto_2 - resto_1) / 1
    print(f"{int(moedas_1)} moeda(s) de 1 real")

    resto_050 = resto_1 % 0.50
    moedas_50 = (resto_1 - resto_050) / 0.50
    print(f"{int(moedas_50)} moeda(s) de 50 centavos")

    resto_010 = resto_050 % 0.1
    moedas_10 = (resto_050 - resto_010) / 0.1
    print(f"{int(moedas_10)} moeda(s) de 10 centavos")

    moedas_001 = round((resto_010) / 0.01)
    print(f"{int(moedas_001)} moeda(s) de 1 centavo")



conta_notas()
