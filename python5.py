#The provided code stub reads and integer, n , from STDIN. For all non-negative integers i < n, print i^2.

n = int(input())
if(1 <= n <= 20):
    for i in range (0,n):
        print(i*i)