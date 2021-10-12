# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 23:18:34 2021

@author: Sukma Julia Nada
"""

a= int(input('Masukkan nilai total harga belanjaan Anda:'))
b= int(input('Masukkan jumlah uang Anda:'))
c= b-a
print("Kembalian Anda sejumlah Rp.",c,'Pecahan uang yang dibutuhkan :')
d= [5000, 2000]
for x in range(0, 2):
    i=0
    while c >= d[x]:
        c = c - d[x]
        i = i+1
        if (i>0):
            print('Uang Rp. %d sebanyak %d lembar' %(d[x], i))