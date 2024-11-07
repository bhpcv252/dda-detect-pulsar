from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

def mean_fits(imgs):
    data = []
    for img in imgs:
        hdulist = fits.open(img)
        data.append(hdulist[0].data)
    
    stacked = np.stack(data, axis=0)
    mean = np.mean(stacked, axis=0)
    return mean


if __name__ == '__main__':
    data  = mean_fits(['image0.fits', 'image1.fits', 'image2.fits','image3.fits', 'image4.fits'])
    
    plt.imshow(data.T, cmap=plt.cm.viridis)
    plt.xlabel('x-pixels (RA)')
    plt.ylabel('y-pixels (Dec)')
    plt.colorbar()
    plt.show()