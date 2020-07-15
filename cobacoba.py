
# def getMode(xs) : # [1,2,2,3,3]
#   countList = []; #1 [1, 1] #2 [2, 1] #3 [2, 2] #4 [3, 1] #5 [3, 2]
#   # create countList

#   for num in xs : # check list (num ; 3)
#     check = False;
#     for list1 in countList : # (cl1 = 0), (cl2 = 1 [1, 1]) (cl3 = [1, 1], [2, 1]) (cl4 = [1, 1], [2, 2]) (cl5 = [1, 1], [2, 2], [3, 1])
#       if(list1[0] == num) : # 3 == 3
#         list1[1] += 1; # menambah frequensi [1, 1] dst.
#         check = True;
#     if(check == False) :
#       countList.append([num, 1]); # tambah ke cl -> value [num, 1]
#   print(countList)
  
#   # create list of mode/s
#   maxFrequency = 0; #2
#   modes = [];
#   for list1 in countList : #([1,1], [2,2], [3,2])
#     if (list1[1] > maxFrequency) : #1 true, #2 true #3 false
#       modes = [list1[0]]; # -> modes [1]
#       maxFrequency = list1[1]; 
#     elif (list1[1] == maxFrequency) : 
#       modes.append(list1[0]); # -> modes [ 2, 3]

#   # if every value appears same amount of times
#   if (len(modes) == len(countList)) : 
#     modes = 'tidak ada modus'

#   if (len(modes)) > 1 :
#     modes = 'tidak ada modus'

#   return modes

# x = [1,2,2,3,3,5,5,4,6,3,7,2,8,9,3]
# print(getMode(x));



# #animal play
# print ('guess the answer')
# score = 0
# angka1= print('angka :', 7)
# hasil = int(input('Berapa pangkat 2 dari angka tersebut? '))
# def check_guess(hasil, benar):
#   if hasil == benar :
#     global score
#     print ('jawaban benar')
#     score +=1
#   else :
#     print('jawaban salah')
# check_guess(hasil, 49)

# angka2= print('angka :', 20)
# hasil = int(input('Berapa pangkat 2 dari angka tersebut? '))
# check_guess(hasil, 400)

# print('score adalah', str(score))

#hangman game

