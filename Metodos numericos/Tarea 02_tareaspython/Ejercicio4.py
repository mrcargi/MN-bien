#Valor presente neto 

print("Programa para calcular el valor presente neto de un proyecto")

invin = float(input("Ingresa la inversion inicial: "))
retornos = []

while True: 
    
    flujos = float(input("ingresa el flujjo de efectivo para cada año en el perido(ingresa '0' para salir):  "))
        
        
    if flujos == 0:
        break
    
    
    retornos.append(flujos)
    
    
tasa = float(input("ingresa la tasa de descuento porcentual %: "))
tasa = tasa/100

vpn = -invin

for i in range(len(retornos)):
    vpn += retornos[i]/ (1+tasa)**(i+1)
    
print(f"El valor presente neto (VPN) del proyecto es : {vpn}")

if vpn <0:
    print("El proyecto NO es viable")
else:
    print("El proyecto SI es viable")