# coding: utf-8
a_list = ['a', 1, 'b', 2]
a_list[0]
print(a_list)
print("First two elements a_list[:2] = " + str(a_list[:2]))
print("Last two elements a_list[-2:] = " + str(a_list[-2:]))
print("Missing left slice index is implicitly 0, missing right slice index is implicitly the length of the list.")
print("e.g. a_list[:] = " + str(a_list[:]))
print("List concatenation temporarily creates another list in memory: [1] + [2] = " + str([1] + [2]))
a_list.append('c')
print("List append: after a_list.append('c'), a_list = " + str(a_list))
a_list.extend([3])
print("List extend: after a_list.extend(3), a_list = " + str(a_list))
a_list.insert(0, 'z')
print("List insert: after a_list.insert(0, 'z'), z inserted at position 0: " + str(a_list))
