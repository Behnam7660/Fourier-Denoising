# Fourier-Denoising
Denoising 1D arrays with FFT algorithm

This function can smooth n number of same-length curves simultaneously with FFT algorithm. 
Input data must be in 3Dshape of : (number of curves, length of curves, 1)
data = data to be smoothed
rate = rate of smoothing. min = 0, max = 1
tail = in order to reduce gibbs phenomenon, a tail with arbitrary length can be added to both sides of the curve

