'''
send and receive numpy array between processes
'''

import numpy as np
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

b = np.array([1])

if rank == 0:
    comm.Recv(b, source=1)
    print("in rank0, receiving b")
    print(b)
else:
    print("in rank1, sending b")
    b = np.array([2])
    print(b)
    comm.Send(b, dest=0)

# mpi cand send and receive numpy array but they have to be of the same size as the one 
# initialized