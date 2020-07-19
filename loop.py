# angka = 1;
# while(angka <= 10) :
#   print(angka);
#   angka += 1
# listItem = list(range(1,11,2));
# print(listItem);

# for item in range(1,11,2):
#   print(item)

# y = ('Nomor Urut ')
# for item in range(1,11) :
#   print(y + str(item))

# for i in range(5) :
#   print(i)

# z = ''
# for item in range (0,5) :
#   z += '*'
# print(z)


# z = ''
# for item in range (0,5) :
#   for item in range (0,5) :
#     z += '*'
#   z += ' \n'  
# print(z)

# z=''
# for item in range(5):
#   for item1 in range(0, item+1):
#     z += "*"
#   z += '\n'
# print(z)

# # z = ''
# # for i in range(5):
# #   for i in range(5, item -1):
# #     z +='*'
# #   z += '\n'
# # print(z)

# # print('\n\n2')
# # a = 6
# # for i in range(0, a):
# #     for j in range(0, a - 1):
# #         print('* ' , end='')
# #     a -= 1
# #     print('')
 
# # print('\n\n3')
# # a = 5
# # s = 2 * a - 2 # for spaces
# # for i in range(0, a):
# #     for j in range(0, s):
# #         print(' ',end='')
# #     s -= 2
# #     for j in range(0, i + 1):
# #         print('* ', end='')
# #     print('')
 
# # print('\n\n4')
# # a = 5
# # s = 0 # for spaces
# # for i in range(0, a):
# #     for j in range(0, s):
# #         # print(j, end='')
# #         print(' ',end='')
# #     s += 2
# #     for j in range(0, a):
# #         print('* ' , end='')
# #     a -= 1
# #     print('')
 
# # print('\n\n5')
# # a = 5
# # s = a - 1 # for spaces
# # for i in range(0, a):
# #     for j in range(0, s):
# #         print(' ', end='')
# #     s -= 1
# #     for j in range(0, i + 1):
# #         print('* ', end='')
 
# #     print('')
 
# # print('\n\n6')
# # a = 5
# # s = 0 # for spaces
# # for i in range(0, a):
# #     for j in range(0, s):
# #         print(' ',end='')
# #     s += 1
# #     for j in range(0, a):
# #         print('* ' , end='')
# #     a -= 1
# #     print('')

# # for i in range(10):
# #     print(('*'*(1+2*i)).center(1+2*10))

# z=''
# for item in reversed(range(5)):
#   for item1 in range(0, item+1):
#     z += "* "
#   z += '\n'
# print(z)

# z=''
# for item in reversed(range(5)):
#   for item1 in range(0, item+1):
#     z += "*"
#   z += '\n'
# for item in (range(4)):
#   for item1 in range(0, item+2):
#     z += "*"
#   z += '\n'
# print(z)

# n=6
# z =''
# for i in range (n):
#   # print("i " + str(i))
#   for j in range (n, i, -1) :
#     # print("j " + str(j))
#     z += " "
#   for k in range (2*i+1) :
#     z += "*"
#   if i == n-2:
#     continue
#   z += '\n'
# print(z)

# n=6
# z =''
# for i in reversed(range (n)):
#   for j in range (n, i, -1) :
#     z += " "
#   for k in range (2*i+1) :
#     z += "*"
#   z += '\n'
# for i in range (n-1):
#   for j in range (n, i+1, -1) :
#     z += " "
#   for k in range (2*(i+1)+1) :
#     z += "*"
#   z += '\n'
# print(z)

# n=6
# z =''
# for i in range (n):
#   for j in range (n, i, -1) :
#     z += " "
#   for k in range (2*i+1) :
#     z += "*"
#   z += '\n'
# for i in reversed(range (n-1)):
#   for j in range (n, i, -1) :
#     z += " "
#   for k in range (2*i+1) :
#     z += "*"
#   z += '\n'
# print(z)

# n = 10
# for i in range(1, n, 2): # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
#     print('-'*(n-i)+ ' *'*i)
# for i in range


# x = 'hello'
# print(x.center(40))


# a = [1,2,3,4,5,6,7,8,9,10]
# i = 1
# while i <=10 :
#   print(list(a**2))
#   i +=1



# a = 0 
# while password == "1234":
#   password = input ('masukan password : ')
#   print('password correct')
#   break
# else: 
#   if password!=1234 :
#     a != 3 
#     a= a+1
#     print('password incorrect')
#     password = input ('masukan password : ')
#   else:
#     print('try again later')



# password = "123"
# while password != "1234":
#   # print('password incorrect')
#   password = input('masukan password : ')
# print ('password correct')


# #soal 1
# for i in range (1,6):
#   if i%2==0:
#     print('wow')
#     continue
#   if i%2!=0 :
#     print(i)


# #soal 2
# def i(a) :
#   for f in range (1,(a+1)) :
#     if f % 3 == 0 and f % 5 == 0:
#         print("fizzbuzz")
#         continue
#     elif f % 3 == 0:
#         print("fizz")
#         continue
#     elif f % 5 == 0:
#         print("buzz")
#         continue
#     else :
#       print(f)
# i(35)


#soal 1
# def isPalindrome(s): 
#   if s.lower() == (s.lower()[::-1]): 
#     print("true") 
#   else: 
#     print('false') 


# isPalindrome('KattAk')


# # soal 2
def level2(s):
  b = ''
  a = s.split(' ')
  for x in a:
      b += x[::-1] + ' '
  print(b)


level2('this is another')


# soal 3

# def morseTranslate(s):
#   dictionaryMorse = {
#   'A':'.- ', 'B':'-... ', 
#   'C':'-.-. ', 'D':'-.. ', 'E':'.', 
#   'F':'..-.', 'G':'--.', 'H':'....', 
#   'I':'..', 'J':'.---', 'K':'-.-', 
#   'L':'.-..', 'M':'--', 'N':'-.', 
#   'O':'---', 'P':'.--.', 'Q':'--.-', 
#   'R':'.-.', 'S':'...', 'T':'-', 
#   'U':'..-', 'V':'...-', 'W':'.--', 
#   'X':'-..-', 'Y':'-.--', 'Z':'--..', 
#   '1':'.----', '2':'..---', '3':'...--', 
#   '4':'....-', '5':'.....', '6':'-....', 
#   '7':'--...', '8':'---.p.', '9':'----.', 
#   '0':'-----', ', ':'--..--', '.':'.-.-.-', 
#   '?':'..--..', '/':'-..-.', '-':'-....-', 
#   '(':'-.--.', ')':'-.--.-', ' ' : '|'
#   }

#   bs = ''
#   for i in s :
#     if dictionaryMorse[i.upper()]:
#       bs +=  dictionaryMorse[i.upper()] 
#   print(bs)


# morseTranslate('abcd')


#soal 4
# def caesar(kata) :
#   abjad = {
#     'a': 'c',
#     'b': 'd',
#     'c': 'e',
#     'd': 'f',
#     'e': 'g',
#     'f': 'h',
#     'g': 'i',
#     'h': 'j',
#     'i': 'k',
#     'j': 'l',
#     'k': 'm',
#     'l': 'n',
#     'm': 'o',
#     'n': 'p',
#     'o': 'q',
#     'p': 'r',
#     'q': 's',
#     'r': 't',
#     's': 'u',
#     't': 'v',
#     'u': 'w',
#     'v': 'x',
#     'w': 'y',
#     'x': 'z',
#     'y': 'a',
#     'z': 'b',
#     ' ': ' ',
#   }

#   sc = ''
#   for i in kata :
#     if abjad[i.lower()] :
#       sc += abjad[i.lower()]
#   print(sc)

  # bs = ''
  # for i in kata :
  #   if abj


#soal no 4

# alphabet =('abcdefghjklmnopqrstuvwxyz')

# caesar = input ('masukkan kata : ')
# key = int(input('masukkan key : '))

# b = ''

# for i in range (len(caesar)) :
#   location = alphabet.index(caesar[i])
#   new = (location+key) % 26
#   b += alphabet[new]

# print(b)
  
# s = ''
# for item in range (1, 6) :
#   for j in range (item, item-1) :
#     s += str(j+1)+ " "
#   s += '\n'
# print(s)

z = ''
for i in range(5,0,-1):
  print(i)
  for i1 in range(i):
      z += str(i1+1) + ' '
  # z += '\n'
print(z)

# from functools import reduce
# number = list(range (1,101))
# n = reduce(lambda a,b : a+b , map(lambda a : a*2, filter(lambda a : a%2 ==0, number)))
# print(n)