num=5
str = f'The number is {num}' if (num<10) else f'The number is greater or equal to {10}'
print(str)

arr=[10, 20, 30, 40, 50]
for i, x in enumerate(arr):
    print(f'On index {i} value is {x}')
