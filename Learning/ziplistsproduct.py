lsta=[1,2,3,4,5]
lstb=[6,7,8,9,10]
lstc=[]
for x, y, in zip(lsta, lstb):
    lstc.append(x*y)
print(lstc)