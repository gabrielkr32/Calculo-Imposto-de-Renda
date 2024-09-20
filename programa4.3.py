salario = float(input("Digite o seu salario para o calculo do imposto: "))
base = salario #eu tenho que utilizar a variavel salario mais de uma vez
imposto = 0 

if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35) #se for superior, calculamos 35%, e armazenamos em 'imposto'
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)

print(f"Salario: R${salario:6.2f} Imposto a pagar: R${imposto:6.2f}")