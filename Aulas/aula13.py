a = 'AAA'
b = 'BB'
c = 1.1
formato = 'a={} b={} c={:.2f}'.format(a,b,c)

print(formato)

string = 'a={} b={} c={:.2f}   {}'
formato2 = string.format(a,b,c, 123)
print(formato2)