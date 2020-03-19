numbers=[6, 0, 2, 2, 1, 4, 1, 5]

def reverselst(lst):
    return lst[-1:-(len(lst)+1):-1]

print(reverselst(numbers)) #doesnot reverse the original list
numbers.reverse() #reverse the original list
print(numbers)
