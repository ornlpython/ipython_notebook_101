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
    data = {'a': np.array([1,2,3])}
    comm.send(data, dest=0)
if rank == 2:
    data = {'b': np.array([10,11,12])}
    comm.send(data, dest=0)

# found a way to send various arrays that have not been initialized in the main code
# this works because we use pickle declaration

#mac102217:MPI j35$ mpiexec -n 3 python pickle_send_recv_mpi_ex4.py
#[{'a': array([1, 2, 3])}, {'b': array([10, 11, 12])}]