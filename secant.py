def f(x):
    return x**2-x-1


def secant(a,b,E):

    i= 1
    condition = True
    while condition:
        if f(a) == f(b):
            print('Divide by zero error!')
            break
        
        m = (a*f(b)-b*f(a))/( f(b) - f(a) ) 
        print('i=%d, a = %0.6f, b = %0.6f, m = %0.6f, f(m)=%0.6f' % (i, a,b,m,f(m)))
        a = b
        b = m
        i = i + 1
        
       
        condition = abs(f(m)) > E
    print("Root: ",m)





a = float(input('Enter First Guess: '))
b = float(input('Enter Second Guess: '))
E = float(input('Tolerable Error: '))



secant(a,b,E)
