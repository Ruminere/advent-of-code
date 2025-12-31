#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>

#define FILE_TO_OPEN "actual.in"

/**
 * Returns the number of digits in num.
 */
long num_digits(long num) {
    if (num == 0) return 1;

    long digits = 0;
    num = labs(num);

    while (num > 0) {
        digits++;
        num /= 10;
    }

    return digits;
}

/**
 * Returns the sum of all valid numbers in the range.
 */
long valid_range(long start, long end, long startseq, long endseq) {
    long sum = 0;

    for (long curseq_num = startseq; curseq_num <= endseq; curseq_num++) {
        long current = pow(10,num_digits(curseq_num))*curseq_num + curseq_num;
        if (current >= start && current <= end) {
            // printf("hit: %ld\n", current);
            sum += current;
        }   
    }

    return sum;
}

/**
 * Splits a number with an even number of digits and returns
 * the upper half of digits.
 */
long split_number(long num, long split) {
    return num/pow(10,split);
}

/**
 * Returns the answer for each range for part 1.
 */
long part1(long start, long end, long multiplier) {
    long start_digits = num_digits(start);
    long end_digits = num_digits(end);
    long split;
    long startseq = 0, endseq = 0;
    if (start_digits % 2 == 0) {
        split = start_digits/2;
        startseq = split_number(start, split);

        if (start_digits == end_digits) {
            endseq = split_number(end, split);
        }
        else {
            endseq = pow(10,split)-1;
        }
    }
    else if (end_digits % 2 == 0) {
        split = end_digits/2;
        endseq = split_number(end, split);
        startseq = pow(10,split-1);
    }
    // printf("valid_range params: %ld, %ld, %ld, %ld\n", start, end, startseq, endseq);

    long sum = valid_range(start, end, startseq, endseq)*multiplier;
    // printf("sum: %ld\n", sum);
    return sum;
}

/**
 * Returns the answer for each range for part 2.
 * C is fast enough lmao I give up on optimization
 */
long part2(long start, long end, long multiplier) {
    long sum = 0;

    long start_digits = num_digits(start);
    long end_digits = num_digits(end);
    long split;

    for (long current = start; current <= end; current++) {
        long current_digits = num_digits(current);
        for (long i = 1; i <= current_digits/2; i++) {
            if (current_digits % i != 0) continue;

            char current_str[32];
            snprintf(current_str, sizeof(current_str), "%ld", current);

            bool hit = true;
            for (long j = 0; j < current_digits; j++) {
                if (current_str[j] != current_str[j%i]) {
                    hit = false;
                }
            }
            if (hit) {
                sum += current;
                break;
            }
        }
    }
    return sum;
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
        // printf("%s\n", line);
    }
    // =============== PROCESS EACH LINE ===============

    // process each range
    for (char* current = strtok(line, ","); current != NULL; current = strtok(NULL, ",")) {
        long start, end;
        bool subtract;

        if (sscanf(current, "%ld-%ld", &start, &end) == 2) {
            // printf("now on: %ld-%ld\n", start, end);
        } else {
            printf("ERROR: badly formatted range: %s", current);
            return 1;
        }

        long multiplier = 1;
        if (start < 0) {
            long tmp = start;
            start = end*-1;
            end = tmp*-1;
            multiplier = -1;
        }

        counter1 += part1(start, end, multiplier);
        counter2 += part2(start, end, multiplier);
    }

    printf("Part 1: %ld\n", counter1);
    printf("Part 2: %ld\n", counter2);

    return 0;
}
