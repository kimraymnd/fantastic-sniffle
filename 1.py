
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

upperbound = 1000
multiple1 = 3
multiple2 = 5
lcm = 15

sum = 0
for x in range (1, upperbound/multiple1+1):
    sum += multiple1*x
for x in range (1, upperbound/multiple2):
    sum += multiple2*x
for x in range (1, upperbound/lcm+1):
    sum -= lcm*x
print sum

#improvements: can use equation n(n-1)/2 for sums instead of iteration
def naturalsum(n):
    return (n*(n+1))/2
print 3*naturalsum(999/3) + 5*naturalsum(999/5) - 15*naturalsum(999/15)
