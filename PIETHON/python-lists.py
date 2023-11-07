x = [0.0, 3.0, 5.0, 2.5, 3.7]
print(type(x))

x.pop(2)
print("x.pop(2)? ",x)

x.remove(2.5)
print("x.remove(2.5)? ",x) 

x.append(1.2)
print("x.append(1.2)? ",x)

y = x.copy()
print("y = x.copy()? ",y)