#serialReadFits

import numpy as np
import timeit
import sys
import glob
import pyfits

start = timeit.default_timer()

data_folder = sys.argv[1]
list_files = glob.glob(data_folder + '/*.fits')
nbr_files = len(list_files)

data = []
for _index, _file in enumerate(list_files):

    hdulist = pyfits.open(_file)
    hdu = hdulist[0]
    _image = np.asarray(hdu.data)
    data.append(_image)

stop = timeit.default_timer()
print("%s took %.2fs to run"%(sys.argv[0], (stop-start)))

#29.14s to run on data/set1/ folder
