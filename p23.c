#include <stdio.h>


char a[28123];
int max = 0;
int isAbundantNumber(int n) {
    if (a[n] == 1) return 1;
    if (n < max) return 0;
    int s = 0;
    for (int i = 1; i < n / 2 + 1; i++) {
        if (n % i == 0)
            s += i;
    }

    if (s > n) {
        a[n] = 1;
        max = n;
        return 1;
    }

    return 0;
}


int main() {
    a[12] = 1;
    int s = 0;
    int can = 0;
    for (int i = 1; i < 28124; i++) {
        can = 0;
        for (int j = 12; j < i / 2 + 1; j++) {
            if (isAbundantNumber(j) && isAbundantNumber(i - j)) {
                can = 1;
                break;
            }
        }
        if (can == 0)
            s += i;
    }

    printf("%d\n", s);
    return 0;
}
