#include <pthread.h>

// define number of threads
#define NUMBER_OF_THREADS 5

// define a multithreading function
void* print(void* thread_id) {
    long tid;
    tid = (long) thread_id;

    cout << "hello world, thread id: " << tid << "\n";

    // terminate
    pthread_exit(NULL);
};

// define threads
pthread_t threads[NUMBER_OF_THREADS];

int rc;
for (int i = 0; i < NUMBER_OF_THREADS; i++) {
    cout << "main(), creating thread:" << i << "\n";

    // create thread
    // pthread_create(thread, attr, start_routine, arg)
    rc = pthread_create(&threads[i], NULL, print, (void*) i);
    if (rc) {
        cout << "error, unable to create thread: " << rc << endl;
        exit(-1);
    }
}

// terminate
pthread_exit(NULL);

// main(), creating thread:0
// main(), creating thread:1
// main(), creating thread:2
// hello world, thread id: 0
// main(), creating thread:3
// main(), creating thread:4
// hello world, thread id: 1
// hello world, thread id: 2
// hello world, thread id: 3
// hello world, thread id: 4