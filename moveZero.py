# def move_zero(num_list):
#     a = [0 for i in range(num_list.count(0))]
#     x = [ i for i in num_list if i != 0]
#     x.extend(a)
#     return(x)

# def movezero(list):
#   kiri= []
#   kanan= []
#   for i in range(len(list)):
#     if list[i] !=0 or type(list[i])==bool:
#       kiri.append(list[i])
#     else:
#       kanan.append(list[i])
#   return(kiri+kanan)

# print(movezero([False,1,0,1,2,3,0,1,3,'a']))
 
def spin(word): 
  b = ''
  a = word.split(' ')
  for x in a:
    if len(x) >= 5: 
      b += x[::-1]+' '
    else :
      b += x + ' '
  return(b)
print(spin('hari ini kamis'))


