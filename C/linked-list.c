// 2023-08

/*
    A linked list implementation in C
*/

#include <stdio.h>
#include <stdlib.h>

// element is struct with value and pointer to the next element
struct Element {
    int value;
    struct Element *next;
};

// allocate memory for element
struct Element *create_element(int value) {
    struct Element *element = (struct Element*)malloc(sizeof(struct Element));
    element->value = value;
    element->next = NULL;
    return element;
}

/*
    operations on this linked list are insert, remove, and print
*/

// insert
void ll_insert(struct Element **element, int value) {
    struct Element *new_element = create_element(value);
    // list is empty
    if (*element == NULL) {
        *element = new_element;
    }
    // list is not empty
    else {
        struct Element *current = *element;
        // iterate until last element
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = new_element;
    }
}

// remove
void ll_remove(struct Element **element, int value) {
    struct Element *current = *element;
    struct Element *previous = NULL;
    // iterate until last element
    while (current != NULL) {
        // value is found
        if (current->value == value) {
            // value is first element
            if (previous == NULL) {
                *element = current->next;
            }
            // value is not first element
            else {
                previous->next = current->next;
            }
            // free memory
            free(current);
            return;
        }
        previous = current;
        current = current->next;
    }
}

// print
void print(struct Element *element) {
    struct Element *current = element;
    // iterate until last element
    while (current != NULL) {
        printf("%d\n", current->value);
        current = current->next;
    }
    printf("NULL\n");
}

int main() {
    struct Element *ll = NULL;
    
    ll_insert(&ll, 5);
    ll_insert(&ll, 10);
    ll_insert(&ll, 15);
    ll_insert(&ll, 20);
    ll_insert(&ll, 25);
    ll_insert(&ll, 30);
    
    print(ll);
    // 5
    // 10
    // 15
    // 20
    // 25
    // 30
    // NULL

    ll_remove(&ll, 15);
    ll_remove(&ll, 30);

    print(ll);
    // 5
    // 10
    // 20
    // 25
    // NULL
}
