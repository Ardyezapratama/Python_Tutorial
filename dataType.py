# a = 10, a merupakan variable dengan nilai 10

#Tipe data: Angka satua tanpa koma(Integer)
data_integer = 1
print("Data : ", data_integer, ", bertipe  : ", type(data_integer))

# Tipe data: float (desimal)
data_float = 1.2
print("Data : ", data_float, ", bertipe : ", type(data_float))

# Tipe data: String (Kumpulan dari karakter)
data_string = "Eza"
print("Data : ", data_string, ", bertipe : ", type(data_string))

# Tipe data: Boolean (true / false)
data_bool = True
print("Data : ", data_bool, ", bertipe : ", type(data_bool))

## Tipe data khusus

# Bilangan kompleks
data_complex = complex(5,6)
print("Data : ", data_complex, ", bertipe : ", type(data_complex))

# Tipe data dari bahasa C
from ctypes import c_double, c_char
data_c_double = c_double(10.5)

print("Data : ", data_c_double, ", bertipe : ", type(data_c_double))

