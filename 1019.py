a=input()
b=a.split('.')
year=int(b[0])
month=int(b[1])
day=int(b[2])
print('%04d.%02d.%02d'%(year,month,day))
