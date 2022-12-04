def f(x):
    return x**2-x-1

def df(x):
    return 2*x-1



def newtonRaphson(b,e):
    if(abs(df(b))==0):
        print("Invalid Choice")
    else:
        m = b-(f(b)/df(b))
        i=1
        while(abs(f(m))>e):
            print('i=%d, b = %0.6f, m=%0.6f, f(m) = %0.6f' % (i, b, m,f(m)))
            b = m
            m = b-(f(b)/df(b))
            i= i+1
        print('i=%d, b = %0.6f, m=%0.6f, f(m) = %0.6f' % (i, b, m,f(m)))
    print("Root: ",m)
        
      


b = float(input('Enter Guess: '))
e = float(input('Tolerable Error: '))



newtonRaphson(b,e)
