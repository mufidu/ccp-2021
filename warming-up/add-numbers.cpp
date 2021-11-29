// # Given two positive integers  and , write a program that add all positive integers between a and b (inclusive). However, since the result of this addition can be too large, you only need to print the result in modulo 10^9 + 7.

// # Input Format

// # The input consists of a single line containing two positive integers a and b.

// # Output Format

// # The output is just a number c which is equal to the sum of all integers between a and b (inclusive) modulo 10^9 + 7.

// # Sample Input 0
// # 5 10

// # Sample Output 0
// # 45
#include <stdio.h>
int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    unsigned long long sum = 0;
    for (int i = a; i <= b; i++) {
        sum += i;
    }
    printf("%llu", sum % 1000000007);
    return 0;
}

// #include <stdio.h>
// int main() {
//     int a, b;
//     scanf("%d %d", &a, &b);
//     unsigned long long sum = 0;
//     sum = (b*(b+1)/2) - (a*(a+1)/2) + a;
//     printf("%llu", sum % 1000000007);
//     return 0;
// }