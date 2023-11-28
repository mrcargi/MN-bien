#Estrategias Especulativas: Bull Spread
from prettytable import PrettyTable 

c1 = 1
c2 = 3
k1 = 30
k2 = 35
s_t = 32



tabla = PrettyTable()

tabla.field_names= ["Precio del Subyacente","Resultado Long Call","Resultado Short Call", "Ganancia o Perdida neta"]

tabla.add_row(["St <= k1", -c1,c2,c2-c1])
tabla.add_row(["k1 <= St < k2",s_t-k1-c1,c2,s_t-k1+c2-c1])
tabla.add_row(["St=>K2",s_t-k1-c1,k2-s_t,k2-k1+c2-c1])

tabla.title = "Bull Spread"
print(tabla)