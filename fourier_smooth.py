import numpy as np
import scipy.fft
import matplotlib.pyplot as plt

data = np.random.random(100)
data_reshaped = np.reshape(data, (1,100,1))

def fourier_smooth(data, rate, tail):
    if np.size(np.shape(data)) < 3:
        data = np.reshape(data, (1, np.shape(data)[0], 1))
    tailzero = np.zeros((np.shape(data)[0],tail,1))
    data = np.append(data, tailzero, axis=1)
    data = np.append(tailzero, data, axis=1)
    # adding tail to handle gibbs phenomenon
    data[:,np.shape(data)[1]-tail:,:] = np.reshape(np.arange(1, tail+1) * [data[:,-tail-1,:] - data[:,-tail-2,:]] + data[:,-tail-1,:], 
                                                   (np.shape(data)[0],tail,1))
    data[:,:tail,:] = np.reshape(-(np.arange(-tail, 0)) * [data[:,tail,:] - data[:,tail+1,:]] + data[:,tail,:], 
                                 (np.shape(data)[0],tail,1))
    # smoothing with fft
    fourier_transformed = scipy.fft.fft(data, axis=1)
    mid = np.shape(fourier_transformed)[1]/2
    fourier_transformed[:, np.int64(np.round(mid - (rate * mid))) : np.int64(np.round(mid + (rate * mid))), :] = 0
    smoothed = scipy.fft.ifft(fourier_transformed, axis=1)
    smoothed = smoothed[:, tail:np.shape(data)[1]-tail, :]
    smoothed = np.real(smoothed)
    return smoothed

smoothed = np.reshape(fourier_smooth(data_reshaped, 0, 0.5), (100))

plt.plot(data)
plt.plot(smoothed)





