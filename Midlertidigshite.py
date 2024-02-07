from pylab import *
from scipy.optimize import curve_fit
# Leser inn dataene
tid = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
vannstand = [94, 43, 26, 61, 113, 138, 111, 59, 35, 64, 117, 146]
# Definerer funksjonen h
def h(t, A, phi, d):
 return A*sin(0.524*t + phi) + d
# Bestemmer konstantene
print(curve_fit(h,tid,vannstand))