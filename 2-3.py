'''     01      '''
a = input()
print(abs(int(a)))


'''     02     '''
a = input().split()
print(min(a))

'''       03        '''
d1, d2, d3, d4, d5 = map(int, input().split())
print(max(d1, d2, d3, d4, d5))



'''    04    '''
#    import math



'''    05    '''
import math
a, b = map(int, input().split())
print(math.sqrt(a**2+b**2))




'''      06       '''

import math
a, b = map(int, input().split())

print(math.factorial(a)/math.factorial((math.factorial(b)*(a-b))))



'''        07         '''
n, m = map(int, input().split())
if (n+m) % 20 == 0:
    print((m+n)//20)
else:
    print((m+n)//20+1)


'''    08    '''
x = input()
print(25//(x*9/10))