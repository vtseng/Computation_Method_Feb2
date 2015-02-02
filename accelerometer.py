__author__ = 'vincent'

from scipy.fftpack import fft
import numpy as np
import cmath
import matplotlib.pyplot as plt
import os

fileNum = 5

dirPath = 'HMP_Dataset/Walk'
fileList = os.listdir(dirPath)

for i in xrange(fileNum):
    walkFile = open(dirPath + '/' + fileList[i])
    #walkFile = open('HMP_Dataset/Sitdown_chair/Accelerometer-2011-03-24-09-50-16-sitdown_chair-f1.txt')
    samples = list()

    line = walkFile.readline()
    while line != '':
        sample = np.array([int(x) for x in line.split(' ')])
        samples.append(np.linalg.norm(sample))
        line = walkFile.readline()

    walkArray = np.array(samples)
    walkfft = fft(walkArray)

    walkMag = list()
    for z in walkfft:
        walkMag.append(cmath.polar(z)[0])

    k = range(len(walkMag))
    plt.subplot(fileNum, 1, i)
    plt.axis([0, 50, 0, 1000])
    #plt.axis([0, 50, 0, max(walkMag)])
    plt.plot(k, walkMag)
plt.show()


