// n, m = map(int, input().split())
// a = list(map(int, input().split()))
// b = list(map(int, input().split()))
// bola_kasihan = 0
// checker = False

// for i in range(n):
//     for j in range(m):
//         if a[i] == b[j]:
//             checker = True
//             break
//     if checker == False:
//         bola_kasihan += 1
//     checker = False

// for i in range(m):
//     for j in range(n):
//         if b[i] == a[j]:
//             checker = True
//             break
//     if checker == False:
//         bola_kasihan += 1
//     checker = False

// print(bola_kasihan)

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, m, i, j, bola_kasihan = 0;
    int *a, *b;
    scanf("%d %d", &n, &m);
    a = (int *)malloc(n * sizeof(int));
    b = (int *)malloc(m * sizeof(int));
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);
    for (i = 0; i < m; i++)
        scanf("%d", &b[i]);
    for (i = 0; i < n; i++)
        for (j = 0; j < m; j++)
            if (a[i] == b[j])
                bola_kasihan++;
    for (i = 0; i < m; i++)
        for (j = 0; j < n; j++)
            if (b[i] == a[j])
                bola_kasihan++;
    printf("%d", bola_kasihan);
    return 0;
}