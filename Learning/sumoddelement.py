#add elements having odd index in the list
distribution = [int(x) for x in input().split(',')]
i=1
sum_distribution=0
for _ in range(int(len(distribution)/2)):
    sum_distribution += distribution[i]
    i+=2
print(sum_distribution)

'''
input = 102, 32, 74, 15, 38, 45, 22
output = 92

input = 42, 24, 32, 11
output = 35

input = 3, 12, 7, 2, 15, 1, 21
output = 15
'''
