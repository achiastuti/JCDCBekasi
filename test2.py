
# n = 5
# z = ''
# for i in range (n):
#   for j in range (n, i, -1) :
#     z += " "
#   for k in range (i) :
#     z += '* '
#   z += '\n'
# print(z)


# def number (num):
#   n = 1
#   for i in range(num):
#     for j in range (num, i, -1):
#       print(' ', end=' ')
#     for k in range(i+1):
#       if n>10 :
#         print(' ',n,end='')
#       else:
#         print(' ',n,end=' ')
#       n += 2
#     print()
#   return 'total baris terakhir adalah', (num**3) 

# print(number(7))

# def ticket(money):
#   change = {25: 0,50: 0,100: 0}
#   for i in money:
#     if i == 25:
#       change[25] += 1
#     elif i == 50:
#       change[50] += 1
#       change[25] -= 1
#     elif i == 100:
#       change[100] += 1
#       if change[50] >= 1:
#         change[50] -= 1
#         change[25] -= 1
#       else:
#         change[25] -= 3
#     if change[25] + change[50] + change[100] < 0 or change[25] <0:
#       return "NO"
#   return "YES"

# print(ticket([25,50,25,50,25,25,25,100]))

# def year (p0,percen,aug,surpuss):
#   time = 0 #initiate time 0

#   while p0 <= surpuss: #while condition
#     p0 = (p0 + (percen * p0) + aug) 
#     time = time + 1

#   return "It took %d year until %d" % (time, surpuss)

# print(year(1000,0.02,50,1200))

# 1000 +20+50=1070
# 1070+21+50=1141
# 1141+22

  

