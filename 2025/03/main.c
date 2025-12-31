#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <ctype.h>

#define FILE_TO_OPEN "actual.in"

/**
 * Returns the answer for each line of part 1.
 */
int part1(char* line) {
    int big1 = 0, idx1 = -1;
    int big2 = 0, idx2 = -1;
    // big1
    for (int i = 0; isdigit(line[i+1]); i++) { // i+1 means last digit isn't detected
        int digit = line[i] - '0';
        if (digit > big1) {
            big1 = digit;
            idx1 = i;
        }
    }
    // big2
    for (int i = idx1+1; isdigit(line[i]); i++) {
        int digit = line[i] - '0';
        if (digit > big2) {
            big2 = digit;
            idx2 = i;
        }
    }
    char num_raw[3];
    sprintf(num_raw, "%d%d", big1, big2);
    // printf("%s\n", num_raw);

    return atoi(num_raw);
}

/**
 * Returns the answer for each line of part 2.
 */
long part2(char* line, int includenum) {
    int len = strlen(line);

    int big[includenum];
    int idx[includenum];
    for (int i = 0; i < includenum; i++) {
        big[i] = -1;
        idx[i] = -1;
    }

    // 1
    for (int i = 0; i <= len-includenum; i++) {
        int digit = line[i] - '0';
        if (digit > big[0]) {
            big[0] = digit;
            idx[0] = i;
        }
    }

    // 2 to 12
    for (int j = 1; j < includenum; j++) {
        for (int i = idx[j-1]+1; i <= len-includenum+j; i++) {
            int digit = line[i] - '0';
            if (digit > big[j]) {
                big[j] = digit;
                idx[j] = i;
            }
        }
    }

    char num_raw[includenum + 1];
    for (int i = 0; i < includenum; i++) {
        num_raw[i] = big[i] + '0';
    }
    num_raw[includenum] = '\0';

    long num = atol(num_raw);
    // printf("%ld\n", num);
    return num;
}

int main()
{
    FILE* input_file;
    char* line = NULL;
    size_t size = 32;

    long counter1 = 0;
    long counter2 = 0;

    input_file = fopen(FILE_TO_OPEN, "r");
    if (input_file == NULL) {
        printf("ERROR: Cannot open %s!", FILE_TO_OPEN);
        return 1;
    }

    // =============== PROCESS EACH LINE ===============
    while (getline(&line, &size, input_file) != -1) {
        size_t len = strlen(line);
        if (len > 0 && line[len-1] == '\n') {
            line[len-1] = '\0';
        }
        // printf("%s\n", line);

        
        // counter1 += part1(line);

        counter1 += part2(line, 2);
        counter2 += part2(line, 12);
    }
    // =============== PROCESS EACH LINE ===============

    printf("Part 1: %ld\n", counter1);
    printf("Part 2: %ld\n", counter2);

    return 0;
}
