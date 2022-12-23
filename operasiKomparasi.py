# Operasi Komparasi
# Setiap hasil dari operasi komparasi adalah True atau False (Boolean)
# >,<,<=,>=,==,!=, is, is not

a = 4
b = 2

# lebih besar dari >
print("=====Lebih Besar Dari (>)=====")
hasil = a > 3
print("a > 3 = ", hasil)
hasil = b > 3
print("b > 3 = ", hasil)
hasil = b > 2
print("b > 2 = ", hasil)


# Kurang dari <
print("=====Kurang Dari (<)=====")
hasil = a < 3
print("a < 3 = ", hasil)
hasil = b < 3
print("b < 3 = ", hasil)
hasil = b < 2 
print("b < 2 = ", hasil)

# Lebih dari sama dengan >=
print("=====Lebih dari sama dengan (>=)=====")
hasil = a >= 3
print("a >= 3 = ", hasil)
hasil = b >= 3
print("b >= 3 = ", hasil)
hasil = b >= 2 
print("b >= 2 = ", hasil)


# Kurang dari sama dengan <=
print("=====Kurang dari sama dengan (<=)=====")
hasil = a <= 3
print("a <= 3 = ", hasil)
hasil = b <= 3
print("b <= 3 = ", hasil)
hasil = b <= 2
print("b <= 2 ", hasil)


# sama dengan ==
print("=====Sama dengan (==)=====")
hasil = a == 4
print("a == 4 = ", hasil)
hasil = b == 4
print("b == 4 = ", hasil)


# tidak sama dengan
print("=====Tidak Sama dengan (!=)=====")
hasil = a != 4
print("a != 4 = ", hasil)
hasil = b != 4
print("b != 4 = ", hasil)

# komparasi object identity (is)
print('=====Object Identity (is)=====')
x = 5 # ini adalah assignment membuat object
y = 5
hasil = x is y
print('x is y = ', hasil)

# is not
print('=====Is Not=====')
x = 5
y = 6
hasil = x is not y
print('x is not y = ', hasil)

