# Given two positive integers  and , write a program that add all positive integers between a and b (inclusive). However, since the result of this addition can be too large, you only need to print the result in modulo 10^9 + 7.

# Input Format

# The input consists of a single line containing two positive integers a and b.

# Output Format

# The output is just a number c which is equal to the sum of all integers between a and b (inclusive) modulo 10^9 + 7.

# Sample Input 0
# 5 10

# Sample Output 0
# 45

a, b = map(int, input().split())
sum = int((b*(b+1)/2) - (a*(a+1)/2) + a)
print(sum%(10**9+7))    
