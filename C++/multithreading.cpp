// 2019-08
#include <iostream>
#include <pthread.h>

#define MAX_THREADS 5

// declare multithreading function
void* print(void* thread_id);
// define multithreading function
void* print(void* thread_id) {
    long tid = (long) thread_id;
    std::cout << "tid: " << tid << std::endl;
    // terminate
    pthread_exit(NULL);
};

int main() {
    pthread_t threads[MAX_THREADS];
    int thread[MAX_THREADS];

    for (int i = 0; i < MAX_THREADS; i++) {
        thread[i] = i;
        std::cout << "creating thread:" << thread[i] << std::endl;
        // create thread using pthread_create(thread, attr, start_routine, arg)
        if (pthread_create(&threads[i], NULL, print, (void*) &thread[i]) != 0) {
            std::cout << "unable to create thread: " << thread << std::endl;
            // fail
            exit(-1);
        }
    }
    // terminate
    pthread_exit(NULL);
    
    // creating thread:0
    // creating thread:1
    // tid: 140701949382784
    // tid: 140701949382788
    // creating thread:2
    // creating thread:3
    // tid: 140701949382792
    // creating thread:4
    // tid: 140701949382796
    // tid: 140701949382800
}