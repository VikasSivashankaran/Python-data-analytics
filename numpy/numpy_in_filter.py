import numpy as np

arr = np.array([41, 42, 43, 44,45])
x = [True,True,True,True,False]
newarr = arr[x]
print(newarr)

filter_arr = arr > 42
newarr = arr[filter_arr]
print("filter arr ",newarr)