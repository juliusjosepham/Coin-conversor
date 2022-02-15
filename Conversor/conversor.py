#funcion para realizar los cálculos.
def monedas(cantidad):
    #monedas de 25 centavos
    quarter = int(cantidad // 0.25)
    balance = cantidad % 0.25

    #monedas de 10 centavos    
    dime = int(balance // 0.10)
    balance = balance % 0.10

    #monedas de 5 centavos
    nickel = int(balance // 0.05)
    balance = balance % 0.05

    #Finalmente, monedas de un centavo
    penny = int(balance // 0.01)
    print (quarter, ' quarters, ', dime, ' dimes, ', nickel, ' nickels, y ', penny, ' pennies.')

dinero = float(input('Ingresa tu cantidad en US$: ')) #Solicitamos el dinero al usuario
print('Ingresaste ', dinero,'US$. Serían:') #Llamamos y mostramos la cantidad

monedas(dinero)

