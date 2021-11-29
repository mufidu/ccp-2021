// n = int(input())
// x = 1
// y = n
// i = 0
// while x < y:
//     i += 1
//     if n % i == 0:
//         x = i
//         y = n//x
// print(y, x)

int main() {
    int n, x, y, i;
    scanf("%d", &n);
    x = 1;
    y = n;
    i = 0;
    while (x < y) {
        i++;
        if (n % i == 0) {
            x = i;
            y = n / x;
        }
    }
    printf("%d %d", y, x);
    return 0;
}