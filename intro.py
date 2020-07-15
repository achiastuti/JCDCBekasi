# # print ('Hello World')

# # print(4/5)
# # print(4//5) # int pembulatan ke bawah

# # #swap
# # x = 2
# # y = 1

# # x, y = y, x
# # print(x,y)

# # # import math
# # print(math.pi)
# # print(math.fabs)
# # print(math.pow)

# # from math import pi, fabs, pow, sqrt,floor,ceil
# # from dipakai saat kita butuh beberapa function saja
# # kita tidak hafal function yang ada dalam module tertentu

# x = 'Halo Dunia Lain'
# print (len(x))
# print(x.index('a'))
# print(x.split('l'))
# print(x.ascii_letters(72))

# #latihan 1
# nama = input ("masukan nama ")
# umur = input ("masukkan umur ")
# print("Nama :" + nama)
# print("Umur :" + umur)
# print(int(umur)%2)
# print(nama[1])

# #latihan 2
# umurA =int(umur)%-2+5
# print(nama[umurA:-1])


# #soal 1
# x = 4
# y = 3
# z = 2

# a={(x+y*z)/(x*y)**z}
# print (a)


# #soal 2
# angka = input ('masukan angka ')
# kuadrat = int(angka)**2
# print (kuadrat)

# #soal 3
# hari = input ('masukan jumlah hari ')
# d = int(hari)
# y= 360
# m= 30
# w= 7
# year = int(d/360)
# month = int(d%360/30)
# week = int(d%360%30/7)
# day = int(d%360%30%7)

# print(str(year) +'Tahun', str(month) + 'Bulan', str(week)+ 'Minggu', str(day)+ 'hari')

# #soal 4
# #usiaAndi + usiaBudi= ab
# #usiaAndi= a
# #usiaBudi= b

# ab = 49
# a = 4
# b = 10
 
# UsiaAndi = (a/(a+b))*ab
# UsiaBudi = (b/(a+b))*ab
# print ('Usia Andi' + str(UsiaAndi+ 2))
# print ('Usia Budi' + str(UsiaBudi+ 2))

# #soal 5
# x = 'Halo Dunia apa Kabar aaaaa' 

# print (len(x.split('a'))-1)


# #soal 6
jarakAB = 120
a = 60
b = 40
go = 9
waktu = jarakAB/(a+b)*60
jam = int(waktu/60)+go
menit = int(waktu%1*60)
print('jam ' + str(jam+go) +' lewat ' +str(menit) + " menit")



# usiaAndi = 40
# usiaAndi *=2
# print(usiaAndi)
# usiaAndi %=2
# print(usiaAndi)

# x = 5
# y = '4'

# print(x==y)
# print(x > int(y))
# print(x < int(y))


# x = 4
# y = '5'
# z = 6

# print(x==int(y) and int(y)<z)
# print(x==int(y) or int(y)<z)
# print(not(x==int(y) or int(y)<z))

angka = input('masukan angka ')
if (int(angka) % 2 == 0) : 
  print("bilangan genap")
else :
  print("bilangan ganjil")







