import multiprocessing as mp
import time

def mult_paralel(a):
    return a[0]*a[1]+a[2]*a[3]

def mult(x,y):
    
    if ( len(y) == 2 ):

        a = pool.map(mult_paralel, [[x[0],y[0],x[1],y[1]]])[0]
        b = pool.map(mult_paralel, [[x[2],y[0],x[3],y[1]]])[0]

        return [a,b]
        
    a = pool.map(mult_paralel, [[x[0],y[0],x[1],y[2]]])[0]
    b = pool.map(mult_paralel, [[x[0],y[1],x[1],y[3]]])[0]
    c = pool.map(mult_paralel, [[x[2],y[0],x[3],y[2]]])[0]
    d = pool.map(mult_paralel, [[x[2],y[1],x[3],y[3]]])[0]
    return [a,b,c,d]

def matrix_power( x, n ):
    if ( n == 1 ):
        return x
    if ( n%2 == 0 ):
        return matrix_power( mult(x, x), n//2 )
    return mult(x, matrix_power( mult(x, x), n//2 ) )


if __name__ == '__main__':

    num_cpus = mp.cpu_count()
    pool = mp.Pool(num_cpus)

    A = [1,1,1,0]
    v = [1,0]

    x = int(input("Tell me the nth number in the Fibonacci sequence you want to calculate: "))
    
    tic = time.perf_counter()
    num = mult(matrix_power(A,x-1),v)[0]
    toc = time.perf_counter()
    
    print(f"Executed in {toc - tic:0.4f} seconds")
    print(num)