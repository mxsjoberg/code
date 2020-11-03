#include <csignal>
// sleep
#include <unistd.h>

// OUTSIDE SCOPE: define signal handler
void terminate(int s) {
   cout << "Interrupt signal: " << s << endl;

   // do something

   exit(s);  
}

// INSIDE SCOPE: register signal
signal(SIGINT, terminate);  

// EXAMPLE: keyboard interrupt
while(1) {
    cout << "Doing something..." << endl;
    sleep(1);
}

// run then ctrl+c 
// Interrupt signal: 2