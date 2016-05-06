'''
send and receive numpy array between processes
'''

import numpy as np
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

a = np.array([1,2,3])

if rank == 0:
    comm.Recv(a, source=1)
else:
    comm.Send(a, dest=0)
