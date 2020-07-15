mobil = ['Alya','Xenia','Avanza'];

print(mobil);
print(mobil[0]);
print(mobil[1]);
print(mobil[2]);
print(mobil[3]); #karena hanya samapai ingdex 2


buah = ['Jeruk', 'Nanas', 'Apel'];
for item in buah :
print("jeruk")


p = [1,2,4,7,9,19]
q = [5,12,16,17,7,9,19,6]
r = [19,6,3,8]

p_set = set (p)
q_set = set (q)
r_set = set (r)


print('gabungan P dan Q :', p_set.union(q_set))
print('gabungan P dan R :', p_set.union(r_set))
print('gabungan Q dan R :', q_set.union(r_set))
print('irisan dari gabungan P dan Q dan gabungan Q dan R', (p_set|q_set)&(q_set|r_set))

buah = ['Jeruk', 'Nanas', 'Apel', 'Mangga'];
buah.append('Kelapa');
print(buah);
buah.pop();
buah.pop();
print(buah);

listTest = [1, 'hi', ['hello', 2, True, [0, 1]]]
print(listTest[1]);
print(listTest[:2]);
print(listTest[2]);
print(listTest[2][1:]);
print(listTest[2][2]);
print(listTest[2][3]);

a = [40, 100, 1, 25, 10]
a.sort(reverse=False)
print(a)

