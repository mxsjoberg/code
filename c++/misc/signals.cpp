#include <iostream>
#include <csignal>
#include <unistd.h>

// signal handler
void terminate(int sig) {
   std::cout << "\nsignal: " << sig << std::endl;
   exit(sig);
}

int main() {
   // register signal
   signal(SIGINT, terminate);  

   // keyboard interrupt
   while(1) {
       std::cout << "stuck doing something really hard... (press ^C to exit)" << std::endl;
       sleep(5);
   }
   // stuck doing something really hard... (press ^C to exit)
   // ^C
   // signal: 2
}