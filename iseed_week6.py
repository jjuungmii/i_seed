#1
read(), readline(), readlines() 

#2
1번

#3 
3, 5

#4
inFp = open("C:/Temp/datal.txt", "r")

inStr = inFp.readme()
print(inStr, end = "")

inFp.close()

#6
inFp = open("C:/Windows/win.ini", "r")
outFp = open("C:/Temp/data3.tct", "w")

inList = inFp.readlines()
for instr in inList :
    outFp.writelines(inStr)
    
inFp.close()
outFp.close()

