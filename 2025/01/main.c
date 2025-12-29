#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char* file_to_open = "test.in";
    FILE* input_file;
    char* line = NULL;
    size_t size = 32;

    input_file = fopen(file_to_open, "r");
    if (input_file == NULL) {
        printf("Cannot open %s!", file_to_open);
        return 1;
    }

    // =============== PROCESS EACH LINE ===============
    while (getline(&line, &size, input_file) != -1) {
        printf("%s", line);
    }
    // =============== PROCESS EACH LINE ===============

    return 0;
}
