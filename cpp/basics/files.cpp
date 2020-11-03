// create and open text-file
ofstream file("test.txt");

// write to file
file << "This is a string.\n";

// read from file to variable
string text;
ifstream file("test.txt");

// read line
getline(file, text);
text
// This is a string.

// or
while (getline(file, text)) {
    cout << text << endl;
};
// This is a string.

// close file
file.close();