def f(x):
    return x**2-x-1


def falsePosition(a,b,E):
    i = 1
    condition = True
    while condition:
        m = (a*f(b)-b*f(a))/( f(b) - f(a) )
        print('i=%d, a= %0.6f, b= %0.6f, m= %0.6f, f(m) = %0.6f, f(a)*f(m)=%0.6f' % (i, a, b, m, f(m),f(a)*f(m)))

        if f(a) * f(m) < 0:
            b = m
        else:
            a = m

        i = i + 1
        condition = abs(f(m)) > E

    print("Root: ",m)





a = float(input('First Guess: '))
b = float(input('Second Guess: '))
E = float(input('Tolerable Error: '))



if f(a) * f(b) > 0:
    print("Invalid Input")
else:
    falsePosition(a,b,E)
