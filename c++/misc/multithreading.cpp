#include <iostream>
#include <pthread.h>

constexpr int max_threads = 5;

void *print(void *thread_id) {
    long tid = (long) thread_id;
    std::cout << "thread_id: " << tid << std::endl;
    // terminate
    pthread_exit(NULL);
};

int main() {
    pthread_t threads[max_threads];
    int thread[max_threads];

    for (int i = 0; i < max_threads; i++) {
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
    // thread_id: 140701949382784
    // thread_id: 140701949382788
    // creating thread:2
    // creating thread:3
    // thread_id: 140701949382792
    // creating thread:4
    // thread_id: 140701949382796
    // thread_id: 140701949382800
}