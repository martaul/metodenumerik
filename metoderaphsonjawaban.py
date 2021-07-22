# -*- coding: utf-8 -*-
"""MetodeRaphsonjawaban

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u6AYNpF9udRHfa3ae8ZzC1SL3YN5aRqw
"""

from math import e #untuk memanggil bilangan eksponen natural (e)
import numpy as np
import matplotlib.pyplot as plt

#mendefinisikan fungsi
def f(x):
	return e**2*x-8*x**2

#mendefinisikan turunan fungsi
def Df(x):
	return 2*e**2*x-16*x

#metode newton raphson
def newtonRaphson(x0,eps):
		step = 0
		print('\n\n*** --Metode Newton raphson-- ***')
		xn = x0
		for n in range(0,100): #maksimal itrasi adalah 100
			fxn=f(xn)
			if abs(fxn) < eps:
				print ('\n akar Persamaan tersebut : %.08f' % xn)
				return xn
			Dfxn=Df(xn)
			if Dfxn == 0:
				print('solusi tidak ditemukan')
				return None
			xn=xn-(fxn/Dfxn)
			step = step + 1
			print('iterasi-%d, x = %0.8f dan f(x) = %0.8f' % (step, xn, f(xn)))
		print('Iterasi maksimum, solusi tidak ditemukan')

#sesi input nilai awal yang dikonversi ke pecahan
x0 = float(input('x0: '))
eps = float(input('epsilon : '))
newtonRaphson(x0,eps)