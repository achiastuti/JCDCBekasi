# angka = input('masukan angka ')
# if (int(angka) % 2 != 0) : 
#   print("bilangan ganjil")
# else :
#   print("bilangan genap")

import math

berat = int(input("berat : "))
tinggi = int(input("tinggi : "))
imt = float(berat/((tinggi/100)**2))
print(imt)

nilai = 0
if (imt > 40) :
  print('obesitas')
elif (imt >= 25 and nilai <= 40) :
  print('BB ideal')
else :
  print("BB kurang")