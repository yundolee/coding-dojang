#중간 복습
#연습문제 + 코딩도장 문제
'''
print('Python Programming')
'''
'''
print(int(0.2467*12+4.159))
'''

#변수 이름으로 첫 문자 숫자/ 키워드 / 특수문자 사용 불가
'''
a,b,c = map(int, input().split())
print(a + b + c)
'''
'''
year = 2000
month = 10
day = 27
hour = 11
minute = 43
second = 59

print(year, month, day, sep = '/', end=' ')
print(hour, minute, second, sep = ':')
'''
#end를 치면 마지막에 실행되는 값이 바뀌는거 생각을 못함
'''
korean = 92
english = 47
mathematics = 86
science = 81

print(korean >= 50 and english >= 50 and mathematics >= 50 and science >= 50)
'''

#s = '''Python is a programming language that lets you work quickly
#and
#integrate systems more effectively.'''

#a = list(range(5, -10, -2))
'''
n = int(input())
a = tuple(range(-10, 10, n))
print(a)
'''
'''
year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
population = [10249679, 10195318, 10143645, 10103233, 10022181, 9930616, 9857426, 9838892]

print(year[-3:])
print(population[-3:])
'''
'''
n = -32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2

print(n[1::2])
'''
'''
del x[-5:]
print(tuple(x))
'''
'''
camille = {
    'health': 575.6,
    'health_regen': 1.7,
    'mana': 338.8,
    'mana_regen': 1.63,
    'melee': 125,
    'attack_damage': 60,
    'attack_speed': 0.625,
    'armor': 26,
    'magic_resistance': 32.1,
    'movement_speed': 340
}

print(camille['health'])
print(camille['movement_speed'])
'''
'''
x=5
if x != 10:
    print('ok')
'''
'''
a= int(input())
b= input()
if b == 'Cash3000':
    print(a-3000)
if b == 'Cash5000':
    print(a-5000)
print(a)
#마지막에 print(a) 삽입 안했는데 왜 실행되냠, 다음부터는 넣자요
'''
#Unit 14
'''
if True:
    print('참')    # True는 참
else:
    print('거짓')
 
if False:
    print('참')
else:
    print('거짓')    # False는 거짓
 
if None:
    print('참')
else:
    print('거짓')    # None은 거짓
'''
'''
x = 10
y = 20

if x == 10 and y == 20:
    print('참')
else:
    print('거짓')
'''
'''
written_test = 75
coding_test = True

if written_test >=80 and coding_test == True:
    print('합격')
else:
    print('불합격')
'''
'''
a,b,c,d = map(int,input().split())
if 0<=a<=100 and 0<=b<=100 and 0<=c<=100 and 0<=d<=100:
    if (a+b+c+d)/4 >= 80:
        print('합격')
    else:
        print('불합격')
else:
    print('잘못된 점수')
'''
'''
x = 30
if x == 10:
    print('10입니다.')
elif x ==20:
    print('20입니다.')
else:
    print('10도 20도 아닙니다.')

'''
#else elif 순서 주의
'''
x = int(input())
if 11<=x<=20:
    print('11~20')
elif 21<=x<=30:
    print('21~30')
else:
    print('아무것도 해당하지 않음') 
'''
'''
age = int(input())
balance = 9000
if 7<=age<=12:
    balance-=650
elif 13<=age<=18:
    balance-=1050
elif age>=19:
    balance-=1250
print(balance)
'''
#코딩할때 잔실수 주의/ 몰랐던 개념은 -=의 활용도가 부족했음/ 실수한 부분은 :의 사용, +,= shift키 잘못 누름..
'''
for i in range(10):
    print('Hello, world!',i)
'''
'''
for i in range(5,12):
    print('Hello, world!',i)

for i in range(10,0,-1):
    print('Hello,world!', i)

for i in reversed(range(10)):
    print('hello, world!',i)

count = int(input('반복할 횟수를 입력하세요: '))
 
for i in range(count):
    print('Hello, world!', i)
'''
'''
a = [10,20,30,40,50]
for i in a:
    print(i)
'''
'''
fruits = ('apple', 'orange', 'grape')
for fruit in fruits:
    print(fruit)
'''
'''
for letter in 'Python':
    print(letter, end=' ')
'''

#for x in y 형식 기억하자(for x in reversed y)
'''
for letter in reversed('Python'):
    print(letter, end=' ')
'''
'''
x = [49,-17,25,102,8,62,21]
for i in x:
    print(10*i, end=' ')

x = int(input())
for i in range(1,10):
    print(x,'*',i, '=', x*i)
'''
'''
i = 0
while i < 10:
    print('Hello, world!')
    i += 1
'''
'''
i = 1
while i <= 100:
    print('Hello,world!',i)
    i+=1
'''
'''
count = int(input('반복할 횟수를 입력하세요: '))

i = 0
while i < count:
    print('Hello,world!',i)
    i +=1
'''
'''
count = int(input('반복할 횟수를 입력하세요: '))

while count > 0:
    print('Hello, world!', count)
    count -= 1
'''

#random
#random.randint(1,6)
'''
import random

i = 0
while i != 3:
    i = random.randint(1,6)
    print(i)
'''

i = 2
j = 5

while i <=32 or j>= 1:
    print(i,j)
    i *=2
    j -=1
