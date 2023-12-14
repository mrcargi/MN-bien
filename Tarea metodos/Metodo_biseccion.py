#APLICACION DEL METODO DE BISECCION 

import sympy as sp
from prettytable  import PrettyTable
from sympy import Function


x= sp.Symbol('x')


fx_str = input("Ingresa la formula:")  #x**3-6*x**2+9*x-3.75
try: 
    fx = sp.sympify(fx_str)
except sp.SympifyError:
    print("invalido")
    exit(1)


print(fx)        #Imprimo la funcion


a = float(input("Define el intervalo a : "))
b = float(input("Define el intervalo b : "))



def biseccion(a,b,error = 0.0001,max_iter= 100):
    if fx.subs(x,a) == 0:
        return a 
    elif fx.subs(x,b) == 0:
        return b
    
    
    if fx.subs(x,a)*fx.subs(x,b) > 0:
        return None
    m_previo = None
    tabla = PrettyTable()
    tabla.field_names=["#Iteracion","a","b","m","f(a)","f(b)","f(m)","Error%"]
    tabla.title = f"METODO DE BISECCION Para la funcion : {fx} "
    m = (a+b)/2 
    
    
    for i in range(max_iter):
        m_previo = m
        m = (a+b)/2 
        errorc = abs(((m) - m_previo)/m) *100
        tabla.add_row([i+1,a,b,m,fx.subs(x,a),fx.subs(x,b),fx.subs(x,m),errorc])
        if errorc == 0:
                errorc = "NA"
        
        
        if fx.subs(x,m) == 0 or (b-a)/2 < error:
            break
        
        
        if fx.subs(x,m) * fx.subs(x,a)< 0:
            b = m
        else :
            a = m
        

            
        # if m_previo is not None:
        #     errorc = (((m) - m_previo)/m) *100
        #     print(f"Iteracion {i + i}: a = {a}, b = {b} , error = {errorc} % , m = {m}")
        # else:
        #     print (f"Iteracion {i + i}: a = {a}, b = {b} , error = NA % , m = {m}")   
        
        
        
    print("Numero maximo de iteraciones alcanzado")
    print(tabla)
    

raiz = biseccion(a,b)
 

