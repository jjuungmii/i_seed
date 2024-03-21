
#4
score = int(input("점수를 입력하세요 : "))

if score >= 90 : 
    print("장학생", end='')
elif score >=60 :
    print("합격", end='')
else : 
    print("불합격", end='')
    
print("입니다. ^^")

#5 
num = 5
if num % 2 == 0 :
    res = '짝수'
else : 
     res = '홀수'
print(res)
-> 2번 res = if num % 2 == 0 '짝수'else'홀수'

#6
nn = [100, 200, 300, 400, 500]

nn[1] = 777 #[100, 777, 300, 400, 500]
nn[1] = [444, 555] #[100, [444, 555], 300, 400, 500]
nn[1:4] = [444, 555] # [100, 444, 555, 500]
nn[2:] = [] # [100, 444]


#8 
hap = 0
n = 1234

while n < 4568:
    if n % 444 == 0:
        hap += n
    n += 1
        
print(hap)

#9
hap = 0

for num in range(3333, 10000):
    if num % 1234 != 0:  # 1234의 배수가 아닌 경우 다음 숫자로 넘어감
        continue
    
    hap += num

    if hap >= 100000:  # 합계가 100000을 넘으면 반복문 종료
        break

print("합계:", hap)

#14
myData = [ [ n*m for n in range(1,3)] for m in range(2, 4)] #-> [[2, 4], [3, 6]]

#5
nn = [100, 200, 300, 400, 500]

nn[4] = 500
nn[-1] = 500
nn[1:4] = 200, 300, 400
nn[0:1] = 100
nn[2:-1] = 300, 400
nn[0::2] = 100, 300, 500
nn[::-1] = 500, 400, 300, 200, 100
nn[::-2] = 500, 300, 100 


