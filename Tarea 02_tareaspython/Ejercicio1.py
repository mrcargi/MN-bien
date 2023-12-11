#Futuros y opciones financieras 
#Crea en python las siguientes funciones y hacer un ejemplo numerico para cada caso 
#(a)Futuro sobre acciones que generan ingresos 
import math
import numpy as np
import scipy.stats as st

def uno():
    print(" Futuro sobre acciones que generan ingreso ")
    try:
        s_o = float(input("Ingrese el precio del activo : "))
        r = float(input("Ingrese la tasa libre de riesgo: "))
        t = float(input("Ingrese tiempo en años: "))
        q = float(input("Ingrese el rendimiento anual: "))
        
        f = s_o*math.exp((r-q)*t)
        print(f)
    except ValueError:
        print("Ingrese un valor numerico")
    
    

def dos():
    print(" Futuro sobre indices ")
    try:
        s_o = float(input("Ingrese el precio del activo : "))
        r = float(input("Ingrese la tasa libre de riesgo: "))
        t = float(input("Ingrese tiempo en años: "))
        q = float(input("Ingrese el rendimiento anual: "))
        
        f = s_o*math.exp((r-q)*t)
        
        print(f)
    except ValueError:
        print("Ingrese un valor numerico ")


def tres():
    print(" Futuro sobre divisas ")
    try:
        
        s_o = float(input("Ingrese el tipo de cambio : "))
        r =float(input("Ingrese el rendimiento  : "))
        t = float(input("Ingrese tiempo en años : "))
        r_f = float(input("Ingrese la tasa libre de riesgo en moneda extrangera : "))
        
        f  = s_o*math.exp((r-r_f)*t)
        print(f)
    except ValueError:
        print("Ingrese un valor numerico ")
def cuatro():
    print(" Futuro sobre commodities que generan costo de almacenamiento ")
    try:
        s_o = float(input("Ingrese el precio spot : "))
        r= float(input("tasa libre de riesgo : "))
        t = float(input("Ingrese el tiempo en años: "))
        
        c = float(input("Ingrese el costo de almacenamiento : "))
        u = c*math.exp(-r*t)
        f = (u+s_o)*math.exp(r*t)

        print(f)
    except ValueError:
        print("Ingrese un valor numerico")
        
def cinco():
    print(" Opcion Call y Put europeas sobre acciones que SI generan ingreso ")
    try:
        tipo = input("Ingrese 'call' o 'put' dependiendo del tipo de opcion que quiera realizar : ")
        tipo = tipo.lower()
        
        s = float(input("Ingrese el precio spot"))             #precio spot
        k = float(input("Ingrese el precio de ejercicio"))     #precio ejercicio
        r = float(input("Ingrese la tasa libre de riesgo"))    #tasa libre de riesgo
        q = float(input("Ingrese el rendimiento"))              #rendimiento
        t = float(input("Ingrese el tiempo en años"))          #tiempo en años
        v = float(input("Ingrese la volatividad") )            #tiempo en años
        d1=((math.log(s/k))+((r-q+(.5*(v**2)))*t))/(v*(math.sqrt(t)))
        d2=d1-(v*(math.sqrt(t)))
        _nd1 = st.norm()
        nd1_=_nd1.cdf(-d1)
        _nd2=st.norm()
        nd2_=_nd2.cdf(-d2)
        
        if tipo == "call":
            c=((s*math.exp(-(q*t)))*nd1_)-((k*math.exp(-(r*t)))*nd2_)
            print("El valor de la opcion call es: ",c)
            
            
        elif tipo =="put":
            p=((k*math.exp(-(r*t)))*nd2_)-((s*math.exp(-(q*t)))*nd1_)
            print ("El valor de la opcion put es : ",p)
        else:
            print("Ingrese una opcion valida")
    except ValueError:
        print("Ingrese un valor numerico")

    
    
def seis():
    try:
        print(" Opcion Call y Put europeas sobre acciones que NO generan ingreso  ")
        tipo = input("Ingrese 'call' o 'put' dependiendo del tipo de opcion que quiera realizar : ")
        tipo = tipo.lower()
        s = float(input("Ingrese el precio spot:  "))             #precio spot
        k = float(input("Ingrese el precio de ejercicio:  "))     #precio ejercicio
        r = float(input("Ingrese la tasa libre de riesgo: "))    #tasa libre de riesgo
        t = float(input("Ingrese el tiempo en años: "))          #tiempo en años
        v = float(input("Ingrese la volatividad: ") )           #tiempo en años
        d1=((math.log(s/k))+((r+(.5*(v**2)))*t))/(v*(math.sqrt(t)))
        d2=d1-(v*(math.sqrt(t)))
        _nd1 = st.norm()
        nd1=_nd1.cdf(d1)
        _nd2=st.norm()
        nd2=_nd2.cdf(d2)
        
        
        if tipo == "call":
            c=(s*nd1)-((k*math.exp(-(r*t)))*nd2)
            print("El valor de la opcion call es : ",c)
        elif tipo == "put":
            p=((k*math.exp(-(r*t)))*_nd2)- (s*_nd1)
            print("El valor de la opcion put es : ",p)
        else:
            print("Ingrese un valor valido")
        
    except ValueError:
        print("Ingrese un valor numerico")




print("----------------MENÚ----------------")
print("(1): Futuro sobre acciones que generan ingreso")
print("(2): Futuro sobre indices")
print("(3): Futuro sobre divisas")
print("(4): Futuro sobre commodities que generan costo de almacenamiento")
print("(5): Opcion Call y Put europeas sobre acciones que no generan ingreso ")
print("(6): Opcion Call y Put europeas sobre acciones que generan ingreso  ")




operacion = input("Ingrese el tipo de operacion a realizar: ")

if operacion == "1":
    uno()
elif operacion == "2":
    dos()
elif operacion == "3":
    tres()
elif operacion == "4":
    cuatro()
elif operacion == "5":
    cinco()
elif operacion == "6":
    seis()
else:
    print("Favore de ingresar un valor valido >:c")
    
    
