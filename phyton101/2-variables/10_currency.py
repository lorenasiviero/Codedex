#this program converts colombian pesos, brazilian reais and peruvian soles currency to dollars
# The user is prompted to enter the amount in the selected currency.
# The program then converts the amount to dollars using the respective conversion rates.
# The conversion rates are:
# 1 Colombian Peso = 0.00021 USD
# 1 Brazilian Real = 0.20 USD
# 1 Peruvian Sol = 0.27 USD

pesos = int(input("Enter the amount in Colombian Pesos: "))
soles = int(input("Enter the amount in Peruvian Soles: "))
reais = int(input("Enter the amount in Brazilian Reais: "))

total = pesos * 0.00021 + soles * 0.27 + reais * 0.20
print("Total in dollars: ", total)