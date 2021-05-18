print("=====LOJAS KAWAYDA=====")
valor_compra = int(input("Preço das compras: R$"))
print(''' FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/ cheque
[ 2 ] à vista cartão 
[ 3 ] 2x no cartão
[ 4 ] 3x no cartão ''')
opc = int(input("Qual é a opção desejada? "))
if opc == 1:
    total = valor_compra - (valor_compra * 10 / 100)
elif opc == 2:
    total = valor_compra - (valor_compra * 5 / 100)
    print("Sua compra de R${:.2f} vai custar R${:.2f} no final.".format(valor_compra, total))
elif opc == 3:
    total = valor_compra
    parcela = valor_compra / 2
    print("Sua compra será parcelada em 2x de R${:.2f} SEM JUROS".format(parcela))
elif opc == 4:
    total = valor_compra + (valor_compra * 20 / 100)
    total_parc = int(input("Quantas parcelas? "))
    parcela = total / total_parc
    print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS".format(total_parc, parcela))
else:
    total = valor_compra
    print("Opção INVÁLIDA de pagamento, tente novamente!")
print("Sua compra de R${:.2f} vai custar  R${:.2f} no final.".format(valor_compra, total))
