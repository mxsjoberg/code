#include <ctime>

// current system time
time_t now = time(0);
// 1604402281

// convert to string
string now_string = ctime(&now);
// Tue Nov  3 12:18:01 2020

// convert to UTC
tm *ltm = localtime(&now);

// year
cout << 1900 + ltm -> tm_year << endl;
// 2020

// month
cout << 1 + ltm -> tm_mon << endl;
// 11

// day
cout << ltm -> tm_mday << endl;
// 3

// time 
cout << 5 + ltm -> tm_hour << ":" << 30 + ltm -> tm_min << ":" << ltm -> tm_sec << endl;
// 17:49:25