// 2019-08
#include <iostream>
#include <csignal>
#include <unistd.h>

// declare signal handler
void terminate(int sig);
// define signal handler
void terminate(int sig) {
   std::cout << "\nsignal: " << sig << std::endl;
   exit(sig);
}

int main() {
   // register signal
   signal(SIGINT, terminate);  

   // keyboard interrupt
   while(1) {
       std::cout << "stuck doing something really hard..." << std::endl;
       sleep(5);
   }
   // stuck doing something really hard...
   // ^C (ctrl+c)
   // signal: 2
}