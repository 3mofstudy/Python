a = input()
b = input()
c = input()
d = input()
print('|{:>10s} {:>10s}|'.format(a,b))  #也可以不寫s--> print('|{:>10} {:>10}|'.format(a,b))
print('|{:>10s} {:>10s}|'.format(c,d))
print('|{:10s} {:10s}|'.format(a,b))    #也可以print('|{:<10s} {:<10s}|'.format(a,b))
print('|{:10s} {:10s}|'.format(c,d))