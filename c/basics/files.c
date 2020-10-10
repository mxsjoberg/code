FILE *file;

// write to file
file = fopen("test.txt", "w+");
fprintf(file, "%s\n", "This is a string.");

// close file
fclose(file);

// read a file
char buffer[255];

file = fopen("test.txt", "r");

// stops at first space
fscanf(file, "%s\n", buffer);
printf("%s\n", buffer);
// This

// stops at newline
fgets(buffer, 255, (FILE*)file);
printf("%s\n", buffer);
// is a string.