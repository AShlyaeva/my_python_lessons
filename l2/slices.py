v = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 2 - шаг, с которым идем по листу.
# print(v[3:8:2])
v1 = v[3:6]
v2 = [v[-1]]
#print(v1, v2, v1 + v2)

# length = len(l)
# print('length', length)
# print(l[length - 1])
# print(l[-1])

# чтобы скопировать массив, а не ссылаться на него, надо так, а не так: arr2 = v
arr2 = v[:]


#list.reverse(v)
v.reverse()
#print(v)

#print(v[1:])
#print(v[:2])
#print(v[::2])
#print(v[-1::-1])
#print(v[::-1])
#print(v)
#print(arr2)
#print(v1)

    
def list_powered(initial_list, power):
    final_list = initial_list[:]
    for i in range(len(initial_list)):
        final_list[i] = initial_list[i] ** power
    return final_list
v4 = list_powered(v, 2)
#print(v4, v)