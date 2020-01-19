def mult_by(list_name, multiplier=1):
	# j = 0
	for i in range(len(list_name)):
		list_name[i] = list_name[i] * multiplier

	# for i in list_name:
	# 	list_name[j] = list_name[j] * multiplier

		# m = 1
		# tmp = ''
		# while m <= multiplier:
		# 	tmp = tmp + list_name[j]
		# 	m = m + 1
		# list_name[j] = tmp

		# j = j + 1
	print('Tadaa')


t = (1, 2, 3, 4, 4)
s = {1, 2, 3, 4, 4}
l0 = [1, 2, 3, 4, 4]

l = ['a', 'b', 'c', 'd']


# length = len(l)
# print('length', length)
# print(l[length - 1])
# print(l[-1])

# mult_by(t, 4)
# print(l)



txt = 'Sasha'
print(txt[0])

our_home_2 = {
	'Sasha': 'Artem',
	'Liza': 'Vitaly',
	333: 'Wow',
	t: 'Not an error!'
}
for item in our_home_2:
	print('dict value is', our_home_2[item])


print(our_home_2[333])
print(our_home_2[(1, 2, 3, 4, 4)])