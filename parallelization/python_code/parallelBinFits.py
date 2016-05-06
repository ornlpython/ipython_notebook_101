#serialBinFits

import numpy as np
import timeit
import sys
import glob
import pyfits
import progressbar

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

start = timeit.default_timer()

data_folder = sys.argv[1]
output_folder = sys.argv[2]

list_files = glob.glob(data_folder + '/*.fits')
nbr_files = len(list_files)
bin_size = 2

# divide by the number of processes
nbr_file_per_job = int(nbr_files / size)

def add(data):
    nbr_array = len(data)
    if nbr_array == 0:
        return data
    else:
        sum_data = data[0]
        for i in range(1, nbr_array):
            sum_data += data[i]
        return sum_data

def export_data(files_to_bin, start_index):

    _files_to_bin = files_to_bin
    data = []
    for _file in _files_to_bin:
        hdulist = pyfits.open(_file)
        hdu = hdulist[0]
        _image = np.asarray(hdu.data)
        data.append(_image)

    sum_data = add(data)

    new_name = output_folder + '/bin_images_%d.fits' % start_index

    hdu = pyfits.PrimaryHDU(sum_data)
    hdu.writeto(new_name)

list_file_for_job = list_files[rank*nbr_file_per_job: (rank+1)*nbr_file_per_job]

nbr_files = len(list_file_for_job)
for _index in np.arange(0, nbr_files, bin_size):
    _files_to_bin = list_files[_index: _index+bin_size]
    data = []
    export_data(_files_to_bin, rank*nbr_file_per_job + _index)

stop = timeit.default_timer()
print("%s took %.2fs to run"%(sys.argv[0], (stop-start)))

# using 2 processors: 53.23s
# using 6 processors: 33s
# using 12 processors: 32s
