with open('numere.txt','r') as f:
    a=f.readline()
    b=f.readline()
if int(a)<int(b):
    print(a)
if int(a)>int(b):
    print(b)
with open('minim.txt','w') as f:
    f.write(str(b)) or (str(a))