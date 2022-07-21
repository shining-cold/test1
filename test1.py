'''a = [1,2,3,4]
print(a)
print(a[2])
a.append(6)
print(a)
a[2] = 2
print(a)
b = a.pop()
print(b)
print(a)
a.pop(3)
print(a)
print(len(a))
print(max(a))
print(min(a))
a.reverse()
print(a)
a.clear()
print(a)'''

#day2
a = [1,2,3,4]
for x in a:
    print(x)
for i in range(len(a)):
    print(i)
    print(a[i])
b= [i*i for i in a]
print(b)
b = [i*i if i<3 else i for i in a]
print(b)

c= (10,20,30,40)
print(c)
print(c[0])
print(c[-1])
print(c[0:2])
print(c[0:-1])
print(c[:])

d = list(c)
print(d)
e = tuple(d)
print(e)




