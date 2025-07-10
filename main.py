'''
Simula el sistema de ventas de una pequeña tienda. El programa debe permitir registrar varios pedidos, cada uno con nombre del cliente, producto y cantidad. Al final, muestra un resumen de ventas
'''
catalogo = {'pan':1000, 'leche':2500, 'huevo':500, 'cafe':1500, 'queso':3000}
lista_pedido = []
# Registrar nombre del cliente
nombre_cliente = input('Indica cual es tu nombre. ').capitalize()

while True:
    print('Nuestro catalogo disponible:')
    # Mostrar nuestro catalogo
    for producto, valor in catalogo.items():
        print(f'{producto}: ${valor}')
    # Registrar el producto del cliente
    producto_deseado = input('Que producto deseas? ').lower()
    # Comprobar que el producto exista
    if producto_deseado not in catalogo:
        print('El producto indicado no fue encontrado')
        continue
    # Ingresar la cantidad de productos que desea
    cantidad = int(input(f'Cuantas unidades de {producto_deseado} quieres? '))
    # Calculo de precio total
    precio_unitario = catalogo[producto_deseado]
    valor_total = precio_unitario * cantidad
    # Almacenamiento de los datos en un diccionario
    datos_pedido = {'producto':producto_deseado, 'cantidad':cantidad, 'total':valor_total}

    lista_pedido.append(datos_pedido)

    print(f'Pedido registrado: {cantidad} de {producto_deseado}\nPor un valor total de: ${valor_total}')

    continuar = input('Deseas ingresar otro producto? Si/No: ').lower()
    if continuar != 'si':
        print('')
        print('')
        print(f'{nombre_cliente}.\nGracias por usar nuestros servicios, ten un excelente dia!')
        break

print('Su pedido:')
for producto in lista_pedido:
    print(f'- {producto['producto']} X {producto['cantidad']} = ${producto['total']}')