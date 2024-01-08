#====================================
# Martinez Castañeda Abner Alfredo
#====================================
# Paradigmas de Programacion
# Matematica Algoritmica
# ESFM IPN DICIEMBRE 2O23
#======================================
from mpi4py import MPI
import math

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

#==========
# Datos
#==========
n = 40
x = range(n)
m = int(math.ceil(float(len(x)) / size))
#=============================================
# Cada proceso tiene un pedazo de los datos
#=============================================
x_chunk = list(x[rank*m: (rank+1)*m])
r_chunk = list(map(math.sqrt, x_chunk))

#=========================================================
# Una sola lista de todos los datos en cada proceso
#=========================================================
r = comm.allreduce(r_chunk)

#============================================================
# Una matriz con todos los datos en cada proceso
#============================================================
rr = comm.allgather(r_chunk)

#===================================================================
# Una matriz con todos los datos pra el proceso 1
#===================================================================
rrr = comm.gather(r_chunk,root=1)

#===================
# Ver lo que paso
#===================
if rank == 0:
    print(r)
    print(rr)
    print(rrr)
if rank == 1:
    print(rrr)
