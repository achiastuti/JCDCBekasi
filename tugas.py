# print(print_number(int(num)))  

# x = input('Masukkan Angka : ')
# angka = { '0' : [' _ ', '| |', '|_|'] ,
#           '1' : ['   ', '  |', '  |'] ,
#           '2' : [' _ ', ' _|', '|_ '] ,
#           '3' : [' _ ', ' _|', ' _|'] ,
#           '4' : ['   ', '|_|', '  |'] ,
#           '5' : [' _ ', '|_ ', ' _|'] ,
#           '6' : [' _ ', '|_ ', '|_|'] ,
#           '7' : [' _ ', '  |', '  |'] ,
#           '8' : [' _ ', '|_|', '|_|'] ,
#           '9' : [' _ ', '|_|', ' _|'] ,
#         }

# y = ''
# for a in range(0,3) :
    
#     for b in x :
#         y += angka[b][a]
            
#     y += '\n'

# print(y)

#tugas 1
# z=''
# for item in reversed(range(1,6)):
#   for item1 in range(5,item-1):
#     z += str(item1)+ ' '
#   z += '\n'
# print(z)

# z=''
# for item in reversed(range(1,6)):
#   for item1 in range(0,item):
#     z += str(item)+' '
#   z += '\n'
# print(z)


# n=6
# z =''
# for i in reversed(range (n)):
#   for j in range (n, i, -1) :
#     z += "  "
#   for k in range (2*i+1) :
#     z += "* "
#   z += ' \n'
# for i in range (n-1):
#   for j in range (n, i+1, -1) :
#     z += "  "
#   for k in range (2*(i+1)+1) :
#     z += "* " 
#   z += '\n'
# print((z))


# n =10
# for i in reversed(range(1, n, 2)):
#     print(' '*(n-i)+ ' *'*i)
# for i in range(3, n, 2): 
#     print(' '*(n-i) +' *'*i)

# tahun = int( input ('tahun : '))
# if tahun%4 == 0 and tahun%400 == 0 :
#   print ('tahun kabisat'),
# elif tahun%4 == 0 and tahun%100 != 0:
#   print ('tahun kabisat')
# else :
#   print ('bukan tahun kabisat')

# studentdata= [
#   {'nama' : 'Andi', 'usia' : 21},
#   {'nama' : 'Budi', 'usia' : 22},
#   {'nama' : 'Caca', 'usia' : 23},
#   {'nama' : 'Deni', 'usia' : 22},
#   {'nama' : 'Edi', 'usia' : 21}
# ]

# class student():
#   def __init__(self, nama, usia):
#     self.name = nama
#     self.age = usia

# studentlist = []


# for i in studentdata :
#   studentlist.append(student(i.get('nama'), i.get('usia')))

# print(studentlist[0].name)
# print(studentlist[1].name)
# print(studentlist[0].age)

# sum = 1
# for i in range (1,11,3) :
#   sum *= i
# print(sum) 


# jumlah = 0
# angka = {1,2,3,4,5,6,7,8,9}
# for i in range (len(angka)+1) :
#   if i %2 != 0 :
#     jumlah += i
# print(jumlah)

# angka = ''
# for i in range (5):
#   for j in range (i) :
#     angka += str (j+1)+" "
#   angka += '\n'
# print (angka)

# class Persegi:
#   def __init__(self,sisi):
#     self.luas = sisi**2
#     self.keliling =sisi*4

# persegi1=Persegi(10)
# print(persegi1.luas)
# print(persegi1.keliling)

# def convert(time):
#   hour = time/3600
#   minutes = time%3600/60
#   second = time%3600%60/60 
#   return '%hour:%minutes:%second'

# import datetime as dt

# def convert(time):
#   return datetime.srftime(%H:%M:%S, datetime.gmtime(time))

# print(convert(3601))
def convert(time): 
  if time > 359999 or time < 0 :
    return "invalid input" 
  else :
    hour = time/3600
    minutes = time%3600/60
    second = time%3600%60 
    return "%02d:%02d:%02d" % (hour, minutes, second) 
  
print(convert(10)) 

