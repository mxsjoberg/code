// 2023-10
#include <iostream>
#include <fstream>
#include <string>

int main() {
    // output stream
    std::ofstream file_out ("_file.txt", std::ofstream::out);
    // write to output stream
    file_out << "the answer is 42\nthis is another line";
    file_out.close();

    // input stream
    std::string line;
    std::ifstream file_in ("_file.txt");
    // read line from input stream
    getline(file_in, line);
    std::cout << line << std::endl;
    // the answer is 42
    file_in.close();

    // read all lines from input stream
    std::string text;
    file_in.open("_file.txt"); // reopen the file
    while (getline(file_in, line)) {
        text += line + "\n";
    };
    std::cout << text << std::endl;
    // the answer is 42
    // this is another line
    file_in.close();
}