#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
    char* file_to_open = "actual.in";
    FILE* input_file;
    char* line = NULL;
    size_t size = 32;
    char current ;

    char direction;
    char turns_raw[4];
    short turns;
    short dial = 50;

    short counter1 = 0;

    input_file = fopen(file_to_open, "r");
    if (input_file == NULL) {
        printf("Cannot open %s!", file_to_open);
        return 1;
    }

    // =============== PROCESS EACH LINE ===============
    while (getline(&line, &size, input_file) != -1) {
        // conversion
        printf("%s", line);
        direction = line[0];
        int i;
        for (i = 1; isdigit(line[i]); i++) {
            turns_raw[i-1] = line[i];
        }
        turns_raw[i-1] = '\0';
        turns = atoi(turns_raw);
        if (direction == 'L') turns *= -1;
        
        printf("%d\n", turns);

        // logic
        dial += turns;
        dial %= 100;
        printf("after: %d\n", dial);
        if (!dial) counter1++;
    }
    // =============== PROCESS EACH LINE ===============

    printf("Part 1: %d\n", counter1);
    return 0;
}
