#import slices
import os
from slices import list_powered
from slices import v1 as old_v1

v = list(range(0, 51))
v1 = list_powered(v, 2)
print(v1, old_v1)
#print(slices.v1)

path = 'C:\\Users\\aspect\\Desktop'
print(os.listdir(path))

for i in range(len(os.listdir(path))):
    print(os.listdir(path)[i])
    print('i is: ', i)
    
for i in os.listdir(path):
    print('i is: ', i)
    
x = 'abcdefg'
for i in x:
    print(i)


# https://docs.python.org/3/library/os.html
#вывести все файлы из папки, у которых расширение mp4, вывести рядом с их названием размер файла.