'''
a = [38,21,53,62,19]
b = (38,21,53,62,19)

r = range(0, 10, 2)
r[2]
'''
'''
a = [0, 0, 0, 0, 0]
a[0] = 38
a[1] = 21
a[2] = 53
a[3] = 62
a[4] = 19
'''

#a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
#슬라이스 a[4:-1]같은 음수의 경우 주의, 음수는 숫자가 작을 수록 큰 수, 절대값 느낌?
#슬라이스는 파이썬 코딩 도장 11.4에 표시되어있는 내용들을 묶는 틀? 여러번 쓰려면 필요해
'''
a[2:8:2] = ['a', 'b', 'c']
a
[0, 10, 'a', 30, 'b', 50, 'c', 70, 80, 90]
del a[2:8:2]
a
[0, 10, 30, 50, 70, 80, 90]
a
[0, 10, 30, 50, 70, 80, 90]
a{2:8:2] = [20,40,60]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
a
[0, 10, 30, 50, 70, 80, 90]
a[2:8:2] = [20,40,60]
a
[0, 10, 20, 50, 40, 80, 60]
a[2:5] = [20,30,40,50]
a
[0, 10, 20, 30, 40, 50, 80, 60]
a[5:] = [50,60,70,80,90]
a
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
'''
'''
year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
population = [10249679, 10195318, 10143645, 10103233, 10022181, 9930616, 9857426, 9838892]

print(year[-3:])
print(population[-3:])
'''
#이런 식으로 -3부터 끝까지 가는 형식이 더 편안함
'''
n = -32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2
13579
print(n[1::2])
'''

#다른 정답 n[1:12:2] or n[1:len(n):2]
'''
x = input().split()
print(x[:-5])
print(tuple(x))
'''
'''
x = input().split()
del x[-5:]
print(tuple(x))
'''
'''
x = input()[1::2]
y = input()[::2]
print(x+y)
'''

#문자열 두 개가 각 줄에 입력된다고 했으면 input을 두번 사용해야함
'''
lux = {'health' : 490, 'mana' : 334, 'melee' : 550, 'armor' : 18.72}
#키가 중복되면 가장 뒤에 있는 값만 사용
lux = {'health' : 490, 'health' : 800, 'mana' : 334, 'melee' : 550, 'armor' : 18.72}
#중복되는 키는 저장되지 않음
'''

#딕셔너리 편하게 만들기(4가지 방법)
'''
lux1 = dict(health=490, mana = 334, melee=550, armor=18.72)
lux1
{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
'''
'''
lux2 = dict(zip(['health','mana','melee','armor'], [490, 334, 550, 18.72]))
lux2
{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
'''
'''
lux3 = dict([('health',490), ('mana',334),('melee',550),('armor',18.72)])

lux4 = dict({'health': 490, 'mana': 334, 'melee':550, 'armor':18.72})
'''
'''
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux['health'] = 2037
lux['mana'] = 1184
lux['mana_regen'] = 3.28

'health' in lux
True
'attack speed' in lux
False
'attack speed' not in lux
True
'''
#len을 이용하여 딕셔너리의 수를 세는게 값의 개수
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
x = input().split()
y = map(float,input().split())
lux = dict(zip(x,y))
print(lux)
'''
#문자 열이 너무 길어질 경우
'''
s = 'dor\
dfsafadf\
adf\
adfddf'
print(s)
'''
'''
x=10
if x == 10:
    print('10입니다')
'''
#들여쓰기 주의하기

#==을 =로 착각하거나 : 안쓰는 경우 주의
'''
x = 10
if x == 10:
    pass    #TODO: x가 10일떄 처리가 필요함
'''

#이런식으로 사용가능함
'''
x = 10

if x == 10:
    print('x에 들어있는 숫자는')
    print('10입니다.')
'''
'''
x = 5

if x ==10:
    print('x에 들어있는 숫자는')
print('10입니다.')
'''

'''

if x >=10:
    print('10 이상입니다.')

    if x == 15:
        print('15입니다.')

    if x == 20:
        print('20입니다.')
'''
'''
x = int(input())

if x ==10:
    print('10입니다')

if x ==20:
    print('20입니다')
'''
'''
x=10

if x != 10:
    print('ok')
'''
