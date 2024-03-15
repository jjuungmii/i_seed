
#1
print("100")
print(100)
print(50+50)
print("50+50")  

#2
print('%d / %d = %d' % ( 5, 10, 5/10))

#3
print("%04d" %876)
print("%5s" % "CookBook")
print("%1.1f" %123.45)

#4
print("{2:d} {0:d} {1:d}" .format(111, 222, 333))

#11

binary_number = '1011'
decimal_from_binary = int(binary_number, 2)
print(decimal_from_binary)

hexadecimal_number = '1A'
decimal_from_hex = int(hexadecimal_number, 16)
print(decimal_from_hex)

#13 
int('1002', 2)
int('1008', 8) #오류 
int('AAFG', 16) 

#15

num = 12345678

print("10진수 ==>", num)

hex_num = hex(num)
print("16진수 ==>", hex_num)


oct_num = oct(num)
print("8진수 ==> ", oct_num)


bin_num = bin(num)
print("2진수 ==> ", bin_num)


