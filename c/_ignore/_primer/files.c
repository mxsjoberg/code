// 2019-08
#include <stdio.h>

int main() {
    FILE *file;

    // write to file
    file = fopen("_file.txt", "w+");
    fprintf(file, "%s\n", "Text to write to file.\n Next line.");
    // close file
    fclose(file);

    // read file
    file = fopen("_file.txt", "r");

    char buffer[255];
    
    // stop read after first space
    // note that reading a word removes it from stream
    fscanf(file, "%s\n", buffer);
    printf("%s\n", buffer);
    // Text

    // stop read after first newline
    fgets(buffer, 255, (FILE*) file);
    printf("%s\n", buffer);
    // to write to file.
}