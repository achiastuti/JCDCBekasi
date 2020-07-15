# import datetime as dt
# class Waktu:
#   hari_bulan_dict = {
#     'Monday' : 'Senin',
#     'Tuesday': 'Selasa',
#     'Wednesday': 'Rabu',
#     'Thursday' : 'Kamis',
#     'Friday' : 'Jumart',
#     'Saturday': 'Sabtu',
#     'Sunday' :'Minggu',
#     'January' : 'Januari',
#     'February' : 'Februari',
#     'March' : 'Maret',
#     'April': 'April',
#     'May' :'Mei',
#     'June': 'Juni',
#     'July':'Juli',
#     'August' :'Agustus',
#     'September':'September',
#     'Oktober':'Oktober',
#     'November':'November',
#     'Desember':'Desember'
#   }
#   time = dt.datetime.now()
#   hari = hari_bulan_dict[time.srftime('%A')]
#   tanggal = time.srftime('%d')
#   bulan = hari_bulan_dict.get(time.srftime('%B'))
#   tahun = time.srftime('%Y')

# sekarang = Waktu()
# print(sekarang.hari)
# print(sekarang.tanggal)
# print(sekarang.bulan)
from functools import reduce
import math
class Statistic:
  def __init__(self, listNum)  :
    self.data = listNum
  def mean(self) :
    #sum = 0 
    sum = reduce(lambda a,b : a+b , self.data)
    # for item in self.data : 
    #   sum += item
    mean = sum / (len(self.data))
    return mean

  def median(self) :
    self.data.sort()
    median = 0
    if (len(self.data) % 2 != 0) :
      median = self.data[math.floor(len(self.data) / 2)]
    else :
      mid1 = self.data[(int(len(self.data) / 2)) - 1]
      mid2 = self.data[int(len(self.data) / 2)]
      median = (mid1 + mid2) / 2
    return median

  def modes(self) : #1,2,3,3,3,5,5,5
    count = []
    for num in self.data : 
      check = False;
      for list1 in count : #(cl1 = 0), (cl2 = 1 [1, 1]) (cl3 = [1, 1], [2, 1]) (cl4 = [1, 1], [2, 1], [3,1]) (cl5 = [1, 1], [2, 1], [3, 2]
        if(list1[0] == num) :
          list1[1] += 1
          check = True
      if(check == False) :
        count.append([num, 1]);
    maxFrequency = 0;
    modes = [];
    for list1 in count :
      if (list1[1] > maxFrequency) : 
        modes = [list1[0]]; 
        maxFrequency = list1[1];
      elif (list1[1] == maxFrequency) : 
        modes.append(list1[0]);
    if (len(modes) == len(count)) : 
      modes = []
    if (len(modes)) > 1 :
      modes = 'tidak ada modus'
    return modes

  def max(self) :
    max = self.data[0]
    for num in self.data :
      if num > max :
        max = num
    return max
    
  def min(self) :
    min = self.data[0]
    for num in self.data :
      if num < min :
        min = num
    return min

stats=Statistic([1,2,3,3,3,5,5,5])
print('Nilai min dari bilangan tersebut adalah ', stats.min())
print('Nilai max dari bilangan tersebut adalah ', stats.max())
print('Nilai mean dari bilangan tersebut adalah ' ,stats.mean())
print('Nilai median dari bilangan tersebut adalah ', stats.median())
print('Nilai modus dari bilangan tersebut adalah ', stats.modes())


