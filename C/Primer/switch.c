// 2019-08
#include <stdio.h>

enum Item {
    LOW = 10,
    MEDIUM = 20,
    ANSWER = 42,
    HIGH = 30
};

const enum Item items[4] = { LOW, MEDIUM, ANSWER, HIGH };

int main() {
    // iterate array of enums
    for (int i=0; i<(sizeof(items) / sizeof(items[0])); i++) {
        switch (items[i]) {
        case 10:
            printf("%s\n", "LOW");
            break;
        case 20:
            continue;
        case 30:
            printf("%s\n", "HIGH");
            break;
        default:
            printf("what is this? %u\n", items[i]);
            break;
        }
    }
    // LOW
    // what is this? 42
    // HIGH
}