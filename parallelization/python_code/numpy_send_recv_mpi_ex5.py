'''
send and receive numpy array between processes
'''

import numpy as np
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data1 = comm.recv(source=1)
    data2 = comm.recv(source=2)

    data = [data1, data2]
    print(data)
if rank == 1:
    data = np.array([1,2,3])
    comm.send(data, dest=0)
if rank == 2:
    data = np.array([10,11,12])
    comm.send(data, dest=0)

# this works also with numpy and will be the right way to retrieve arrays 
# calculated in various processors

#mac102217:MPI j35$ mpiexec -n 4 python numpy_send_recv_mpi_ex4.py
#[array([1, 2, 3]), array([10, 11, 12])]