// boolean variables
bool T = true;
bool F = false;

// and, or
T || F                  // 1
T && (T && F)           // 0

// not
!T                      // 0
!(!T)                   // 1

// relational
1 == 2                  // 0
1 != 2                  // 1
1 > 2                   // 0
1 < 2                   // 1
1 >= 2                  // 0
1 <= 2                  // 1

// bitwise operators
int A = 60;             // 0011 1100
int B = 13;             // 0000 1101

A & B                   // 12, 0000 1100
A | B                   // 61, 0011 1101
A ^ B                   // 49, 0011 0001
~A                      // -61, 1100 0011
A << 2                  // 240, 1111 0000
A >> 2                  // 15, 0000 1111