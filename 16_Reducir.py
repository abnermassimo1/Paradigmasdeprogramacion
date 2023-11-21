#==============================
# Martinez Castañeda Abner
#==============================
# Paradigmas de programacion
# Matematica Algoritmica
# ESFM IPN OCTUBRE 2023
#===============================

#===============================================
# Uso de reducciones (colapsar resultados)
#===============================================

#=============================================================
# Multiplicacion de todos los numeros en la lista
#=============================================================

from functools import reduce

bigdata = [2,3,5,7,11,13,17,19,23,29]

#================
# Funcion x*y
#================

multiplicar = lambda x,y: x*y
suma = lambda x,y: x + y

print(reduce(multiplicar,bigdata))
print(reduce(suma,bigdata))

#==========================================================
# Reduce e aplica la funcion por pares a los resultados y 
# el siguiente elemento comensando con los dos primeros 
# elementos.
#==========================================================

