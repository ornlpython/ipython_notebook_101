#passRandomDraw.py

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

randNum = np.zeros(1)

if rank == 1:
    randNum = np.random.random_sample(1)
    print("Process %d drsw the number %f"%(rank, randNum[0]))
    comm.Send(randNum, dest=0)

if rank == 0:
    print("Process %d before receiving has the number %f"%(rank, randNum[0]))
    comm.Recv(randNum, source=1)
    print("Process %d after receiving has the number %f"%(rank, randNum[0]))

