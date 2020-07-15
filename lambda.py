# input = [2,4,6,8]
# j = map(lambda x: x**2, input)
# print(list(j))


# word = input('masukan kata : ')
# words_list = ['merdeka', 'hello', 'sohib', 'kari ayam', 'pesawat', 'mobil', 'loker', 'kamar', 'saya', 'motor', 'pertamax', 'merah'] 
# m = list(filter(lambda a: word in a, words_list))
# print(m)

# angka = [1,2,3,4,5]
# n = list(map(lambda a:a*2, filter(lambda a : a>3, angka)))
# print(n)

# def faktorial(x): 
#   if x == 1: 
#     return 1 
#   else: 
#      return (x*faktorial(x-1)) 
# bil = int(input('angka : '))
# print("Faktorial dari", bil, " adalah", str(faktorial(bil)))

# def faktor(x) :
#   for i in range(1, x+1):
#     if x % i == 0:
#       print(i)
# faktor(20)

# def factor(x):
#   nums = (range(1, x+1))
#   n = list(filter(lambda x: x%nums==0, nums))
#   return n
# print(factor(5))

# min = 1
# max = 100
# prima =[]
# for n in range(min,max+1):
#   if n > 1: 
#       for i in range(2,n): 
#         if (n % i) == 0: 
#           break 
#       else:
#         prima.append(n) 
# print(prima)

from functools import reduce 
number = list(range (1,101))
n = reduce(lambda a,b : a+b , map(lambda a : a*2, filter(lambda a : a%2 ==0, number)))
print(n)



