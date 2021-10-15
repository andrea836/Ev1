import datetime
from collections import namedtuple
# Lo usaremos con lista ya que se nos hace mejor que un diccionario
# para este caso, obviamente un diccionario es mejor pero aqui no ocupamos
# keys y/o atributos para esta ya q tenemos el namedtuple, sabemos que si
# se puede hacer pero se nos facilita mejor con una lista 
Registros = namedtuple("Registros","folio, fecha")
lista_registros = []
Ventas = namedtuple("Ventas","folio_registro, descripcion, cantidad, precio, subtotal")
lista_ventas = []

folio = 0

contador = True
while contador:
    print("*****MENU*****")
    print("1.Registrar una venta")
    print("2.Consultar una venta")
    print("3.Salir")
    opcion= int(input("¿Que accion deseas realizar?: "))

    if opcion == 1:
        total = 0
        fecha = datetime.date.today()
        folio = folio +1
        folio_registro = folio
        dato_en_turno = Registros(folio, fecha)
        lista_registros.append(dato_en_turno)     
        while True:
            print("\nRegistrar una venta")
            descripcion = input("Dime el nombre del articulo: ")
            cantidad = int(input("Dime la cantidad del articulo: "))
            precio = int(input("Dime el precio del articulo: "))
            subtotal = cantidad * precio
            print(f"Subtotal: {subtotal}")
            dato_en_turno = Ventas(folio_registro, descripcion, cantidad, precio, subtotal)
            lista_ventas.append(dato_en_turno)
            respuesta = int(input("\n¿Quieres agregar algun otro dato? 1[si], 2[no]: "))
            if respuesta != 1:
                for elemento in lista_ventas:
                    if elemento.folio_registro == folio:
                        total += elemento.subtotal  
                IVA = total*.16+total        
                print(f'Total: {total}')
                print(f'Total con IVA: {IVA}')
                break
        
    elif opcion == 2:
        total = 0
        IVA = 0
        print("\nConsultar una Venta")
        folio_a_buscar = int(input("Dime el folio que quieras consultar : "))
        print("-"*30)
        for elemento_r in lista_registros:
            if elemento_r.folio == folio_a_buscar:
                print(f'Folio: {elemento_r.folio}')
                print(f'Fecha: {elemento_r.fecha}')
        print('Descripcion \t Cantidad \t Precio \t Subtotal')    
        for elemento in lista_ventas:
            if elemento.folio_registro == folio_a_buscar:
                print(f'{elemento.descripcion} \t {elemento.cantidad} \t\t {elemento.precio} \t\t {elemento.subtotal}')
                total += elemento.subtotal
        IVA = total*.16+total
        print(f'Total: {total}')
        print(f'Total con IVA: {IVA}') 
        print()
        print("-"*30)
                   
    elif opcion >= 3:
        print("\nAdios")
        contador = False
    
    else:
        pass
        
