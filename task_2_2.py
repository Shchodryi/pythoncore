a = int(input("enter 4-character digit: "))
a_list = list(str(a))
multi = eval('*'. join(a_list))
a_list.reverse()
rev = (''.join(a_list))
sorting = ''.join(sorted(str(a)))
print(multi)
print (rev)
print(sorting)