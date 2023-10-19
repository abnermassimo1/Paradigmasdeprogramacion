#=============================================
#   Martinez Castañeda Abner Alfredo
#=============================================
#   Matematica Algoritmica
#   Paradigmas de Programacion
#   ESFM IPN Octubre 2023
#============================================

#=====================================================
#   La clase CienteBancario esta en el subdirectorio
#   aplicacion/banco/
#=====================================================
from aplicacion.banco.cliente_bancario import ClienteBancario

#===========================================================
# try: intenta(correr las instrucciones)
# except: atrapar el error en una variable e
# e se puede convertir a string
#============================================================
#  Error por sacar mas dinero del que tiene
#============================================================
try:
  cliente = ClienteBancario("Jaime Andrade", "Hernandez Sanchez", 28, 0.0)
  cliente.guardarDinero(300)
  print(cliente.imprimirInfo())
  cliente.retirarDinero(400)
  print(cliente.imprimirInfo())
#==============================================================
# Exception es el objeto mas general del error
#==============================================================
except Exception as e:
    print("Error: " + str(e))

#==========================================================
#   Error por usar un atributo privado
#==========================================================
try:
  print(cliente.__nombres)
except Exception as ex:
  print("Error: " + str(ex))

#==========================
#  Forma correcta
#========================
print(cliente.nombres)
