#serialBinFits

''' 
This file bin all the files of a given directory by the number of files defined as first argument,
then the input folder as second argument and the output folder as last argument

'''

import numpy as np
import timeit
import sys
import glob
import pyfits
import progressbar

start = timeit.default_timer()

bin_size = int(sys.argv[1])
data_folder = sys.argv[2]
output_folder = sys.argv[3]

list_files = glob.glob(data_folder + '/*.fits')
nbr_files = len(list_files)

def add(data):
    nbr_array = len(data)
    if nbr_array == 0:
        return data
    else:
        sum_data = data[0]
        for i in range(1, nbr_array):
            sum_data += data[i]
        return sum_data
    

pbar = progressbar.ProgressBar(widgets=[progressbar.Percentage(), progressbar.Bar()], 
                               maxval=nbr_files).start()
for _index in np.arange(0, nbr_files, bin_size):

    _files_to_bin = list_files[_index: _index+bin_size]
    data = []
    for _file in _files_to_bin:
        hdulist = pyfits.open(_file)
        hdu = hdulist[0]
        _image = np.asarray(hdu.data)
        data.append(_image)
            
    sum_data = add(data)

    new_name = output_folder + '/bin_images_%d.fits' % _index

    hdu = pyfits.PrimaryHDU(sum_data)
    hdu.writeto(new_name)

    pbar.update(_index)

pbar.finish()

stop = timeit.default_timer()
print("%s took %.2fs to run"%(sys.argv[0], (stop-start)))

#process took 67.47 !!!!
