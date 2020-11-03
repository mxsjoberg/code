try {
    // do something

    throw 0;
} catch (int error) {
    // do something
    
    cout << "Error: " << error << endl;
    // Error: 0
}

// EXAMPLE: default exception
bool error = true;
try {
    if (!error) {
        // do something
    } else {
        // error code
        throw 0;
    }
} catch (...) {
    cout << "Default exception." << endl;
    // Default exception.
}