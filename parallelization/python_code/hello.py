# hello.py

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

#print("Number of processes is %d" %comm.Get_size())   # '4' if 'mpiexec -n 4 python hello.py'
#print("Hello world from process %d" %rank)

# (py3)mac102217:MPI j35$ python hello.py
# -> Hello world from process 0

# (py3)mac102217:MPI j35$ mpiexec -n 5 python hello.py
#Hello world from process 0
#Hello world from process 3
#Hello world from process 4
#Hello world from process 2
#Hello world from process 1
