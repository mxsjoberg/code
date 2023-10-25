// allocate an array of n elements of size s
// 	void *calloc(int n, int s);

// release a block of memory specified by address
// 	void free(void *address);

// allocate an array of b bytes and leave uninitialised
// 	void *malloc(int b);

// re-allocate memory extending to new size s
// 	void *realloc(void *address, int s);

// allocating memory dynamically
char name[100];
char *description;

strcpy(name, "Adam Warlock");

// allocate memory dynamically
description = malloc(10 * sizeof(char));

// handle error
if (description == NULL) {
    fprintf(stderr, "%s\n", "Error: Unable to allocate memory.");
} else {
    strcpy(description, "Adam Warlock is more powerful than Thanos.");
}

// printf("Name: %s\n", name);                           // Name: Adam Warlock
// printf("Description: %s\n", description);             // Description: Adam Warlock is more powerful than Thanos.

// re-allocate memory to store a longer description
description = realloc(description, 100 * sizeof(char));

if (description == NULL) {
    fprintf(stderr, "%s\n", "Error: Unable to allocate memory.");
} else {
    strcat(description, " This is some additional description.");
}

printf("Name: %s\n", name);                             // Name: Adam Warlock
printf("Description: %s\n", description);               // Description: Adam Warlock is more powerful than Thanos. This is some additional description.

// release memory
free(description);