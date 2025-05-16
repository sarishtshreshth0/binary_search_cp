import math
import heapq
from heapq import heappop, heappush
MOD = 10**9 + 7

## power
def power(x, y, p=MOD):
    res = 1
    while y:
        if y & 1: res = res * x % p
        x = x * x % p
        y //= 2
    return res

## XOR upto n
def xor_upto(n):
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n + 1
    else:  # n % 4 == 3
        return 0

## gcd and lcm
def gcd(a, b): return math.gcd(a, b)
def lcm(a, b): return (a * b) // gcd(a, b)

## prefix sum
def prefix_sum(arr):
    psum = [0] * (len(arr) + 1)
    for i in range(len(arr)): psum[i+1] = psum[i] + arr[i]
    return psum

## number of set bits 
def number_of_set_bits(n):
    count = 0
    while n > 0:
        n = n & (n - 1)
        count += 1
    return count

def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

#kadane's algo , maximum sub
def maximum_subarray_sum(l):
    sums = 0
    maxi = -10**9
    for i in l:
        sums += i
        maxi = max(maxi, sums)
        if sums < 0:
            sums = 0
    return maxi


#Ceil Precision Code
def ceil_div(a, b):
    return (a + b - 1) // b

def number(): return int(input())
def numbers(): return map(int , input().split())
def lists(): return list(map(int, input().split()))
def s(): return input()

##-------------------------------------------------------------------##
