# Casting (merubah dari satu tipe data ke tipe data lainnya)

## INTEGER
print("=====INTEGER=====")
data_int = 5
print("data = ", data_int, " type = ", type(data_int))

data_bool = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #Akan bernilai false jika nilai int = 0
print("Data = ", data_bool, ", type = ", type(data_bool))
print("Data = ", data_str, ", type = ", type(data_str))
print("Data = ", data_bool, ", type = ", type(data_bool))

## FLOAT
print("=====FLOAT=====")
data_float = 5.5
print("Data = ", data_float, ", type = ", type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)
print("Data = ", data_int, ", type = ", type(data_int))
print("Data = ", data_str, ", type ", type(data_str))
print("Data = ", data_bool, ", type = ", type(data_bool))


## BOOLEAN
print("=====BOOLEAN=====")
data_bool = True
print("Data = ", data_bool, ", type = ", type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)
print("Data = ", data_int, ", type = ", type(data_int))
print("Data = ", data_str, ", type ", type(data_str))
print("Data = ", data_float, ", type = ", type(data_float))


## STR
print("=====STRING=====")
data_str = "10"
print("Data = ", data_str, ", type = ", type(data_str))

data_int = int(data_str) # String harus angka
data_flaot = float(data_str) # String harus angka
data_bool = bool(data_str) #false jika string kosong
print("Data = ", data_int, ", type = ", type(data_int))
print("Data = ", data_float, ", type ", type(data_float))
print("Data = ", data_bool, ", type = ", type(data_bool))