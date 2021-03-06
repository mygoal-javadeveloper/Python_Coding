# Enter your code here. Read input from STDIN. Print output to STDOUT
x, y = list(map(int, input().split()))
midline = int(x // 2)
midpoint = int(y // 2)
countdash = 1
countpoint = 1
welcomestr = 'WELCOME'

for i in range(0, midline):
    for j in range(midpoint - countdash):
        print('-', end='')
    for n in range(0, countpoint):
        print('.|.',end = '')
    for s in range(midpoint - countdash):
        print('-', end='')
    print()
    countdash = countdash + 3
    countpoint = countpoint + 2
middash = ((y//2) - 3)
for x in range(0, middash):
    print('-', end='')
for y in range(0, len(welcomestr)):
    print(welcomestr[y], end='')
for x in range(0, middash):
    print('-', end='')
print()
for i in range(0, midline):
    countdash = countdash - 3
    countpoint = countpoint - 2
    for j in range(midpoint - countdash):
        print('-', end='')
    for n in range(0, countpoint):
        print('.|.',end = '')
    for s in range(midpoint - countdash):
        print('-', end='')
    print()
    
    '''
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be NxM. ( N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

input = 9 27
'''
