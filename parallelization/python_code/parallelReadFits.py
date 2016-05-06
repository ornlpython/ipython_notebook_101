#parallelReadFits

import numpy as np
import timeit
import sys
import glob
import pyfits
from mpi4py import MPI
from mpi4py.MPI import ANY_SOURCE

comm = MPI.COMM_WORLD
rank = comm.Get_rank() # process index
size = comm.Get_size() # number of processes available

def load_fits(start_index, list_files):
    _data = np.empty((len(list_files)), dtype=np.object)
    for _index, _file in enumerate(list_files):
        hdulist = pyfits.open(_file)
        hdu = hdulist[0]
        _image = np.asarray(hdu.data)
        np.append(_data, _image)
    return _data

start = timeit.default_timer()

# retrieve list of files to load
data_folder = sys.argv[1]
list_files = glob.glob(data_folder + '/*.fits')
nbr_files = len(list_files)

data = np.empty((nbr_files), dtype=object)
recv_buffer = np.zeros(1)

file_step = int(nbr_files / size)

_list_files = list_files[(rank-1)*file_step:(rank-1)*file_step+file_step]
_loading = np.empty((len(_list_files)), dtype=np.object)
_loading = load_fits((rank-1)*file_step, _list_files)

if rank == 0:
    final_array = data
    for i in range(1, size):
        comm.Recv(recv_buffer, ANY_SOURCE)
#        _data = recv_buffer
#        _start_index = (rank-1)*file_step
#        _len = len(_list_files)
#        data[_start_index:_start_index+_len] = _data
else:
    comm.Send(_loading, dest=0)

stop = timeit.default_timer()
print("%s took %.2fs to run"%(sys.argv[0], (stop-start)))

#29.14s to run on data/set1/ folder
