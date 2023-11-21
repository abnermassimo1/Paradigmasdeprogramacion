#==================================
# Martinez Castañeda Abner Alfredo
#==================================
# Paradigmas de programacion
# Matematica Algoritmica
# ESFM IPN OCTUBRE 2023
#==================================


#=============================================
# yield transforma la funcion a iterador
#=============================================
def migenerador():
    print("Primero")
    yield 10
    print("Segundo")
    yield "20"
    print("Tercero")
    yield "hola"


#====================================
# gen es un iterador
#====================================

gen = migenerador()
vall = next(gen)
print(vall)
val2 = next(gen)
print(val2)
val3 = next(gen)
print(val3)

