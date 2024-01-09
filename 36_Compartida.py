#=========================================
# Martinez Castañeda Abner Alfredo
#=========================================
# Paradigmas de Programacion
# Matematica Algoritmica
# ESFM IPN DICIEMBRE 2023
#==========================================

#=====================================================================
# Las colas(queues) son memorias compartidas entre procesos
#=====================================================================
from multiprocessing import Process,Queue

def cubico(x,q):
    # Poner en la memoria compartida una tupla(x,x_cubica)
    q.put((x,x*x*x))

#===================
# Codigo principal
#===================
if __name__=="__main__":

    # q es una cola(memoria compartida)
    q = Queue()

    #=========================================
    # INSTANCIAR UNA LISTA DE PROCESOS
    #=========================================
    procesos = [Process(target=cubico,args=(i,q)) for i in range(1,10)]

    for p in procesos:
        p.start()

    for p in procesos:
        p.join()

    #=======================================================================
    # Metodo get (les pido a los procesos que me den su resultado en la cola)
    # No nos da el rresultado en orden hay que ponerle identificador
    #=======================================================================
    resultado = [q.get() for p in procesos]

    print(resultado)
