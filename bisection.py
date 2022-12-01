a = float(input('a: '))
b = float(input('b: '))
E = float(input('E: '))


def f(x):
    return x**2-x-1

def bisection(a,b,E):
    i = 1
  
    condition = True
    while condition:
        m = (a + b)/2
        print('i=%d, a=%0.6f, b= %0.6f, m = %0.6f, f(m) = %0.6f, f(a)*f(m)=%0.8f' % (i, a, b,m, f(m),f(a)*f(m)))

        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
        
        i = i + 1
        condition = abs(f(m)) > E

    print('Root: %0.8f' % m)


if f(a) * f(b) > 0.0:
    print("Invalid Input")
else:
    bisection(a,b,E)











            
            
            
    
