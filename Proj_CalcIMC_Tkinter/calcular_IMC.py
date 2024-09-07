def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso, altura = map(str, input('Digite o seu peso e sua altura com espaco: ').split())

peso = float(peso)
altura = float(altura)

imc = calcular_imc(peso, altura)
print(f'Seu IMC e: {imc:.2f}')