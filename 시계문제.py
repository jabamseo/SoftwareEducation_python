import math

#문제1
print("문제 1. 시침, 분침 사이의 각")
print("시와 분을 입력하시오")
hour1 = int(input("시 : "))
min1 = int(input("분 : "))
fst_degree = abs((hour1*30+min1*(0.5)-min1*6)%360) #시침, 분침 사이의 각
if 360-fst_degree > fst_degree: #예각 찾는과정
  real_degree = fst_degree
else:
  real_degree = 360-fst_degree
print(f"결과 : {real_degree}도\n")

#문제2
print("문제 2. 시침, 분침 겹치는 시간")
print("몇시와 몇시를 입력하시오")
fst_hour = int(input("시 : "))
snd_hour = int(input("시 : "))
for hour2 in range(fst_hour,snd_hour):
  min2 = math.floor(hour2*30/5.5) #'hour*30+min*0.5=min*6'에서 유도
  if min2 < 60:
    print(f'결과 : {hour2}시 {min2}분')
  else:
    print(f'결과 : {hour2+1}시 {min2-60}분')
    
#문제3
print("\n문제 3. 시침과 분침이 이루는 각도")
print("각도를 입력해 주세요.")
degree = int(input("각도 : "))
for hour3 in range(0,12):
  m1 = math.floor(hour3*30 - degree)/5.5
  m2 = math.floor(hour3*30 + degree)/5.5
  m3 = math.floor(hour3*30 + degree-360)/5.5
  m4 = math.floor(hour3*30 - degree+360)/5.5

  a = [m1,m2,m3,m4]
  a = set(a); a = list(a)
  a.sort()

  for j in a:
    if j < 0 or j >=60:
      pass
    if j >= 0 and j<60:
      j = math.floor(j)
      print(f'{hour3}  :  {j}')