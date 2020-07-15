

def calc(x,y,z) :
  if y == '+' :
    print(x+z)
  elif y == '-' : 
    print(x-z)
  elif y == '*' :
    print(x*z)
  elif y == '/' :
    print(x/z)
  elif y == '**' :
    print(x**z)

calc(2,'+',10)


def segitiga(a,t) :
  print(a*t*1/2)
  
segitiga(10,6)

def total(x,y) : 
  z = x + y
  print (z)

print(total(4,5))

def kali(x) :
  if (x < 2) :
    return 1;
  else :
    return (x * tiga());

def tiga() :
  return 3;

print(kali(5));
print(kali(100))

def switch(x):
  x.lower()
  x = x.replace('a','o')
  x = x.replace('i','o')
  x = x.replace('u','o')
  x = x.replace('e','o')
print(switch('aiueo'))


def fungsi(x):
  return 0
def fungsi2 (x,y) :
  return 0
def fungsi3 (z) :
  return 0
def fungsi4 () : 
  return 0

contoh = [{'Test_1':[{0 : print('berhasil')}]}]
z = 0
y = 0
x = 0

contoh[fungsi(x)]['Test_1'][fungsi2(x,y)][fungsi3(z)[fungsi4()]]
