#APLICACION DEL METODO DE FALSA POSICION


import sympy as sp

from prettytable  import PrettyTable


x= sp.Symbol('x')
fx =(sp.exp(x)) + (2**(-1*(x))) + 2 * sp.cos(x) - 6
print(fx)        #Imprimo la funcion






def falsa_posicion(a,b,error = 0.000001,max_iter= 100):
    if fx.subs(x,a).evalf() == 0:
        return a 
    elif fx.subs(x,b) == 0:
        return b
    
    
    if fx.subs(x,a).evalf()*fx.subs(x,b).evalf() > 0:
        return None
    m_previo = None
    tabla = PrettyTable()
    tabla.field_names=["#Iteracion","a","b","m","f(a)","f(b)","f(m)","Error%"]
    tabla.title = f"METODO DE FALSA POSICION Para la funcion : {fx} "
    
    for i in range(max_iter):
        
        m = b - ((fx.subs(x, b)).evalf() * (b - a) / (fx.subs(x, b).evalf() - fx.subs(x, a).evalf()))

        
        
        if fx.subs(x,m).evalf() == 0 or abs(fx.subs(x,m).evalf()) < error:
            break
        
        
        if fx.subs(x,m).evalf() * fx.subs(x,a).evalf()< 0:
            b = m
        else :
            a = m
        
        if m_previo is not None:
            errorc = (((m) - m_previo)/m) *100
        else:
            errorc = "NA"
            
        
            
        tabla.add_row([i+1,a,b,m,fx.subs(x,a).evalf(),fx.subs(x,b).evalf(),fx.subs(x,m).evalf(),errorc])
        
             

        # if m_previo is not None:
        #     errorc = (((m) - m_previo)/m) *100
        #     print(f"Iteracion {i + i}: a = {a}, b = {b} , error = {errorc} % , m = {m}")
        # else:
        #     print (f"Iteracion {i + i}: a = {a}, b = {b} , error = NA % , m = {m}")   
        
        m_previo = m
    print("Numero maximo de Iteraciones alcanzado")
    print(tabla)

a = 1.5
b = 2


raiz = falsa_posicion(a,b)


