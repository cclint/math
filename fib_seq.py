''' the input n represents a reference to a particular fibbonacci number in the fibbonacci sequence.

The Fibonacci Sequence is a mathematical function such every 
number is the sum of the two preceding numbers, starting 
from 0 and 1. 

F_0 = 0, F_1 = 1 
 
 and 

 F_n = F_n-1 + F_n-2, for n > 1.
 
  Here is list of the first 10 numbers in the sequence: (0,)1,1,2,3,5,8,13,21,34,89'''

def fib(n):
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = 100
print(fib(n))



