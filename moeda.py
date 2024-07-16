Real = int(input('Digite um valor em real: '))
Dolar = int(input('Digite um valor em dólar: '))
Euro = int(input('Digite um valor em euro: '))

real1 = Real/5.45
print('O valor de real para dólar é de US${:.2f}'.format(real1))

real2 = Real/5.88
print('O valor de real para euro é de {:.2f}'.format(real2))

dolar1 = Dolar/5.25
print('O valor de dólar para real é de R${:.2f}'.format(dolar1))

dolar2 = Dolar/1.08
print('O valor de dólar para euro é de {:.2f}'.format(dolar2))

euro1 = Euro/0.17
print('O valor de euro para real é de R${:.2f}'.format(euro1))

euro2 = Euro/1.08
print('O valor de euro para dólar é de US${:.2f}'.format(euro2))