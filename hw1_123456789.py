import numpy as np
import matplotlib.pyplot as plt
import cv2

def histImage(image):
    histogram = np.zeros(256, int)

    for row in image:
        for pix in row:
            histogram[pix] +=1
    
    return histogram

def nhistImage(image):
    normalHistogram = histImage(image)
    normalHistogram = normalHistogram / np.sum(normalHistogram)

    return normalHistogram

def ahistImage(image):
    accHistogram = histImage(image)
    
    accHistogram = np.cumsum(accHistogram)
    accHistogram = accHistogram.transpose()

    return accHistogram

def calcHistStat(histogram):
    mean = np.mean(histogram)
    var = np.var(histogram)
    return mean, var

def mapImage(image,toneMap):
    newImage = np.clip(toneMap[image], 0, 255)    

    return newImage

def histEqualization(image):
    tempHistogram = np.zeros(256, int)
    histogram = np.zeros(256, int)

    return image
