#===========================================
# Martinez CAstañeda Abner Alfredo
#===========================================
#  Matematica Algoritmica
#  Paradigmas de programacion
#  ESFM IPN DCIEMBRE 2023
#=============================================
from mpi4py import MPI
import numpy

#===================================================
# Enviar objeto mensaje con comunicacion bloqueada
# (cada proceso espera a que le reciban su mensaje)
#===================================================
class Mensaje:
    def __init__(self,rank):
        #iterador
        self.x = range(rank*10)
        #string
        self.p =  "vengo del proceso " +str(rank)

#======================
# Programa pincipal
#======================
if __name__== "__main__":
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()
    s = Mensaje(rank)

    #=============================================================
    #  Que te mande el anterior y si es cero que sea el ultimo
    #=============================================================
    fuente = rank-1 if rank!=0 else size-1

    #=======================================================================
    # Mandalo al siguiente y si eres el ultimo mandalo al primero
    #=======================================================================
    destino = rank+1 if rank!=size-1 else 0

    #=========================================================================
    # send y recv son operaciones bloqueadas y generan que el
    # codigo se atore esperando que alguien reciba un mensaje
    # esto se resuelve enviando con los pares y recibiendo con los impares
    #=========================================================================

    # Si soy par
    if rank%2==0:
        #=================================
        # Enviar mensaje s al dest
        #=================================
        comm.send(s, dest=destino)

        #==============================================
        # Recibir de source y lo pone en m
        #==============================================
        m = comm.recv(source=fuente)

    # Si no soy par
    else:
        #=================================================
        # Recibir primero y mandar mensaje despues
        #=================================================
        m = comm.recv(source=fuente)
        comm.send(s,dest=destino)

    print("Soy el proceso ", rank, ", el resultado es", len(m.x),",",m.p)

    #===================================================================
    # Para una comunicacion mas rapida se utilizan arreglos de numpy
    # (send y recv van con mayuscula y cambian un poco)
    # Se indica el ripo de datos explicitamente
    #===================================================================
    #  EJEMPLO 1 USANDO ENTEROS
    #==============================
    if rank == 0:
        #============================================
        # Arreglo de enteros del 0 al 9
        #============================================
        data = numpy.arange(10, dtype='i')
        #==================================================
        #Envio bloqueante especificando el tipo de dato
        #==================================================
        comm.Send([data, MPI.INT], dest=1, tag=77)
    elif rank == 1:
        data = numpy.empty(10, dtype='i')
        comm.Recv([data, MPI.INT], source=0, tag=77)
        print(data)
    #==============================================================
    # Tambien se puede sin decir el tipo de dato pero deben
    # concidir el tipo de arreglos a los extremos del mensaje
    #==============================================================
    #  EJEMPLO 2 USANDO FLOTANTES
    #==============================
    if rank == 0:
        data = numpy.arange(10, dtype=numpy.float64)
        comm.Send(data, dest=1,tag=13)
    elif rank == 1:
        data = numpy.empty(10, dtype=numpy.float64)
        comm.Recv(data, source=0, tag=13)
        print(data)



