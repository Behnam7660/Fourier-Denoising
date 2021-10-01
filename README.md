# Fourier-Denoising_1D
Denoising 1D arrays with FFT algorithm

This function can smooth n number of same-length curves simultaneously with FFT algorithm.

Input data must be in 3Dshape of : (number of curves, length of curves, 1)

data = data to be smoothed

rate = rate of smoothing. min = 0, max = 1

tail = in order to reduce gibbs phenomenon, a tail with arbitrary length can be added to both sides of the curve


![Example1](https://user-images.githubusercontent.com/72737338/135656066-1e44f301-1e8f-46d5-b946-659267cccc47.png)

![Example2](https://user-images.githubusercontent.com/72737338/135656119-46f7f7b3-0ea6-44c8-9b16-85ba716f4fb9.png)

