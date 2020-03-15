# Enter your code here. Read input from STDIN. Print output to STDOUT
x, y = list(map(int, input().split()))
midline = int(x / 2)
midpoint = int(y / 2)
welcomestr = 'WELCOME'

for i in range(0, x):
    j = 0
    while j < y:
        if i == 0:
            if j == 0:
                print('|', end = '')
                j = j + 1
                continue
            elif j == (y-1):
                print('|')
                j = j + 1
                continue
            else:
                print('-', end = '')
                j = j + 1
                continue
        elif i == (x-1):
            if j == 0:
                print('|', end = '')
                j = j + 1
                continue
            elif j == (y-1):
                print('|')
                j = j + 1
                continue
            else:
                print('-', end = '')
                j = j + 1
                continue
        elif i == midline:
            if j == midpoint - 3:
                for k in range(0, len(welcomestr)):
                    print(welcomestr[k], end = '')
                j = j + len(welcomestr)
                continue
            elif j % 2 == 0:
                if j != (y-1):
                    print('|', end = '')
                    j = j + 1
                    continue
                else:
                    print('|')
                    j = j + 1
                    continue
            else:
                if j != (y-1):
                    print('-', end = '')
                    j = j + 1
                    continue
                else:
                    print('-')
                    j = j + 1
                    continue
        elif j % 2 == 0:
            if j != (y-1):
                print('|', end = '')
                j = j + 1
                continue
            else:
                print('|')
                j = j + 1
                continue
        else:
            if j != (y-1):
                print('-', end = '')
                j = j + 1
                continue
            else:
                print('-')
                j = j + 1
                continue
        
            
'''
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be NxM. ( N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.

input = 9 27
'''