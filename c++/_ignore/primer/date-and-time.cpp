// 2023-10
#include <iostream>
#include <string>
#include <ctime>

int main() {
    // current system time
    time_t now = time(0);

    // print friendly
    std::cout << ctime(&now) << std::endl;
    // Fri Oct 27 05:23:19 2023

    // convert to local
    tm *local_datetime = std::localtime(&now);

    std::cout << 1900 + local_datetime -> tm_year << std::endl;
    // 2023
    std::cout << 1 + local_datetime -> tm_mon << std::endl;
    // 10
    std::cout << local_datetime -> tm_mday << std::endl;
    // 27
    std::cout << 5 + local_datetime -> tm_hour << ":" << 30 + local_datetime -> tm_min << ":" << local_datetime -> tm_sec << std::endl;
    // 10:55:33
}