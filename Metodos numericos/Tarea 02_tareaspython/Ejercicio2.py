#Elabore un program en python que permita aplicar tasas de descuentos a productos de acuerdo a su precio de venta.


tasas = [0.12,0.20,0.35]


def descuento (preciop):
        
        
    if 0<preciop<=15000:
        return preciop*tasas[0]
        
    elif 15000<preciop<=35000:
        return preciop*tasas[1]
        
    else:
        return preciop*tasas[2]
        


while True:
    try:  
        preciopr = (input("Favor de ingresar el precio (o 'exit' para salir ): "))
        if preciopr.lower() == "exit":
            break
        preciopr= int(preciopr)
        
        desc = descuento(preciopr)
        print(f"El descuento aplicado fue de : {desc}")
    except ValueError:
        print("Favor de ingresar un valor valido ")
        