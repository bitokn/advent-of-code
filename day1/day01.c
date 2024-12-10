#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    FILE *fp = fopen(*(argv + 1), "r");

    int left[1000] = {};
    int right[1000] = {};

    for (int i = 0; i < 1000; i++) {
        fscanf(fp, "%d%d", &left[i], &right[i]);
    }

    for (int i = 1; i < 1000; ++i) {
        // float key = GMArray[i];
        // int key2 = prodIDArray[i];
        // int jey = sortedProdIDArray[i][0];
        // int key3 = profitArray[i];

        int key = left[i];

        int j = i - 1;
        while (j >= 0 && left[j] < key) {
            left[j + 1] = left[j];
            j -= 1;
        }
        left[j + 1] = key;
    }

    for (int i = 1; i < 1000; ++i) {
        // float key = GMArray[i];
        // int key2 = prodIDArray[i];
        // int jey = sortedProdIDArray[i][0];
        // int key3 = profitArray[i];

        int key = right[i];

        int j = i - 1;
        while (j >= 0 && right[j] < key) {
            right[j + 1] = right[j];
            j -= 1;
        }
        right[j + 1] = key;
    }

    int distarr[1000];

    for (int i = 0; i < 1000; i++) {
        // printf("%d %d\n", left[i], right[i]);

        distarr[i] = left[i] - right[i];
    }
    int sum = 0;
    for (int i = 0; i < 1000; i++) {
        if (distarr[i] < 0) {
            sum += -distarr[i];
        } else {
            sum += distarr[i];
        }
    }
    printf("%d\n", sum);

    int similarity[1000];
    for (int i = 0; i < 1000; i++) {
        int count = 0;
        for (int j = 0; j < 1000; j++) {
            if (right[j] == left[i]) {
                count += 1;
            }
        }
        similarity[i] = left[i] * count;
    }
    int sum2 = 0;
    for (int i = 0; i < 1000; i++) {
        if (similarity[i] < 0) {
            sum2 += -similarity[i];
        } else {
            sum2 += similarity[i];
        }
    }
    printf("%d\n", sum2);

    fclose(fp);
    return 0;
}
