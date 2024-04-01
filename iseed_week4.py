
#5 
ss = 'Python' 
for i in range(0, len(ss)): 
        print(ss[i]+ '%', end ='')  
        
#11




#9 
inStr, outStr = "python", "" 
strLen = len(inStr) 

for i in range(0, strLen) : 
    outStr += inStr[strLen-(i+1)] 
print("내용을 거꾸로 출력 --> %s" % outStr) 

#13 
import turtle 
import random 
import math 

swidth, sheight = 500, 500 
txtSize = 20 
center_radius = 200
num_of_rotations = 2  # 두 바퀴 회전

turtle.title('거북이 나선형 글자 쓰기') 
turtle.shape('turtle') 
turtle.setup(width=swidth + 50, height=sheight + 50) 
turtle.screensize(swidth, sheight)	  
turtle.penup() 

inStr = turtle.textinput('문자열 입력', '거북이 쓸 문자열을 입력') 

num_chars = len(inStr)
max_radius = min(swidth, sheight) / 2 - txtSize * 2
total_angle = 360 * num_of_rotations
angle_step = total_angle / num_chars

for i, ch in enumerate(inStr): 
    angle = i * angle_step
    radian = math.radians(angle)

    radius = center_radius * (total_angle - angle) / total_angle
    tX = radius * math.cos(radian)
    tY = radius * math.sin(radian)

    r = random.random()
    g = random.random()
    b = random.random() 

    turtle.goto(tX, tY) 
	 
    turtle.pencolor((r, g, b)) 
    turtle.write(ch, font=('맑은고딕', txtSize, 'bold')) 

turtle.done()

#3 
def plus(v1,v2,v3) :
    result = 0
    result = v1 + v2 + v3
    return result 
    
hap = plus(100, 200, 300)
print(hap)

#4
var = 100
def f1() :
    print(var)
    
def f2() :
    var = 10 
    print(var)

#11
def addNumber(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return total

print(addNumber(100))  # 출력: 5050

#8
def myFunc(p1=1, p2=2, p3=3 ) : 
    ret = p1 + p2 + p3
    return ret

print("매개변수 없이 호출 ==>", myFunc())
print("매개변수가 1개로 호출 ==>",  myFunc(1))
print("매개변수가 2개로 호출 ==>",  myFunc(1, 2))
print("매개변수가 3개로 호출 ==>",  myFunc(1, 2, 3))


















