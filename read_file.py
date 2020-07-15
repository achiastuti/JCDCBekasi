# data = open('coba.txt', 'r+')
# print (data.read())
# #  print(data.readlines())
# data.write('aku')


# data_diri = open('daftar_nama.csv','r')
# x = data_diri.read()
# print(x) 

# json = open('daftar_nama.json', 'r')
# print (json.read())

# import json
# with open('daftar_nama.json','r') as daftar :
#   output = json.load(daftar)

# print(output)
# for i in range(len(output)):
#   print(output[i])

# with open('daftar_nama_copy.json','w') as copy :
#   json.dump(output,copy)

# import csv
# list_data = []
# with open('daftar_nama.csv', mode='r') as nama:
#     read = csv.DictReader(nama)
#     for data in read:
#         list_data.append(dict(data))
# print(list_data)

# with open('daftar_nama_copy.csv', mode='w', newline='') as nama_copy:
#     columns = list_data[0].keys()
#     write = csv.DictWriter(nama_copy, fieldnames=columns)
#     write.writeheader()
#     write.writerows(list_data)



# import json
# import csv

# #import json to csv
# with open('daftar_nama.json','r') as nama:
#   read = json.load(nama)
#   print(read)

# with open('json_to_csv.csv','w', newline='') as nama_copy:
#   columns = read[0].keys()
#   write = csv.DictWriter(nama_copy, fieldnames=columns)
#   write.writeheader()
#   write.writerows(read)

#import csv ke json
# list_data = []
# with open('daftar_nama.csv', mode='r') as nama:
#     read = csv.DictReader(nama)
#     for data in read:
#       list_data.append(dict(data))

# with open('csv_to_json.json', mode='w') as copy:
#     json.dump(list_data, copy)



# Soal
# 1. diawali dengan 4, 5, 6
# 2. 16 digit
# 3. 0-9
# 4. tanda hubung '-'
# 5. berulang lebih 3x berurutan

import json

# with open('nasabah.json','r') as data_nasabah:
#   nasabah = json.load(data_nasabah)
#   a = list(nasabah[0].keys())
#   cr1 = 0
#   cr2 = 0
#   valid = []
#   invalid = []
  

#   for i in nasabah:
#     cc = i.get(a[1])
#     sp = cc.split('-')
#     gabung= ''.join(sp)
#     # if cc[0] in '456' :
#     #   if len (cc) == 16 and cc.isdigit():
#     #     valid.append(i)
#     #   elif len(cc) !=16 and cc[4] == '-' and cc[9] == '-' and cc[14] == '-' : 
#     #     valid.append(i)
#     #   for x in range(len(gabung)-4):
#     #     if gabung[x:x+4] != gabung[x]*4:
#     #       valid.append(i)
#     # else : 
#     #   invalid.append(i)
    
#     if cc[0] in '456' :
#       if len(cc) == 16 or len(cc) == 19 :
#         check = '0123456789-'
#         for k in cc :
#           if k not in check :
#             invalid.append(i)
#         if len(cc) == 19 :
#           check2 = '0123456789'
#           for l in sp :
#             if len(l) != 4 :
#               invalid.append(i)
#         for m in range(len(gabung)-4) :
#           if gabung[m:m+4] == gabung[m]*4 :
#             invalid.append(i)
#         valid.append(i)  
#     invalid.append(i)
          
        

      #   invalid.append(i)
  # print(len(valid))
    # valid.append(x)
    # print(valid)
    # # Criteria 1 & 2 & 3
    # for k in cr1:
    #   if cc[0] == k :
    #     if len(cc) == 16 and cc.isdigit() :
    #       valid.append(i)
    #     else :
    #       invalid.append(i)
    #     break
    #   else:
    #     if cc[4] == '-' and cc[9] == '-' and cc[14] == '-' :
    #       valid.append(i)
    #     else :
    #       invalid.append(i)
    #     break
  
    # # Criteria 4
    # if cc[4] == '-' and cc[9] == '-' and cc[14] == '-' :
    #   # print ('C4 ', i)
    #   valid.append(i)
    # else :
    #   invalid.append(i)
  # print('valid ', valid)
  # print(len(invalid))

  # b = (nasabah[0].get(a[]))
  # print(b)

# with open('valid.json','w') as valid :
#   json.dump(nasabah,valid)

    
    
    # if len(number) == 16 and number.isdigit() :
    #   for m in range(len(gabung)-4) :
    #     if gabung[m:m+4] == gabung[m]*4 :
    #       return False
    #   return True
  #   if len(number) == 16 or len(number) == 19 :
  #     if number.isdigit() :
  #       # for m in range(len(gabung)-4) :
  #       #   if gabung[m:m+4] == gabung[m]*4 :
  #       #     return False
  #       return True
  #     if number[4] == '-' and number[9] == '-' and number[14] == '-' :
  #       return True
  #     # for l in numberSpl :
  #     #   if len(l) != 4 :
  #     #     return False
  #     for m in range(len(gabung)-4) :
  #       if gabung[m:m+4] == gabung[m]*4 :
  #         return False
  #     return True
  # return False
  
  # if cc1[0] in '456' :
  #   if len(cc1) == 16 or len(cc1) == 19 :
  #     check = '0123456789-'
  #     for k in cc1 :
  #       if k not in check :
  #         return False
  #     if len(cc1) == 19 :
  #       check2 = '0123456789'
  #       for l in numberSpl :
  #         if len(l) != 4 :
  #           return False
  #     for m in range(len(gabung)-4) :
  #       if gabung[m:m+4] == gabung[m]*4 :
  #         return False
  #     return True
  # return False



def CheckValidation(number):
  numberSpl = number.split('-')
  gabung= ''.join(numberSpl)
  print(gabung)

  if number[0] in '456' :
    if len(number) == 16 and number.isdigit() :
      for m in range(len(gabung)-4) :
        if gabung[m:m+4] == gabung[m]*4 :
          return False
      return True
    if len (number) == 19 and number[4] == '-' and number[9] == '-' and number[14] == '-' :
      for m in range(len(gabung)-4) :
        if gabung[m:m+4] == gabung[m]*4 :
          return False
      return True
  return False


print(CheckValidation('4234-5678-9101-11'))


# with open('nasabah.json','r') as data_nasabah:
#   nasabah = json.load(data_nasabah)
#   a = list(nasabah[0].keys()) # ['nama', 'NoCC']
#   valid =[]
#   invalid=[]
#   for i in nasabah:
#     cc = i.get(a[1]) # i['NoCC']
#     if CheckValidation (cc) :
#       valid.append(i)
#     else :
#       invalid.append(i)


# with open('valid.json', 'w') as data_valid:
#   json.dump(valid, data_valid)

# with open('invalid.json', 'w') as data_invalid:
#   json.dump(invalid, data_invalid)









