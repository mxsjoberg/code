PROGRAM records;
TYPE
    // define record type
    People = record
        _id: integer;
        _name: string;
        _email: string;
    END;
VAR
    // declare variables
    Person_1, Person_2: People;
BEGIN
    // initialise record
    Person_1._id := 1;
    Person_1._name := 'Adam';
    Person_1._email := 'adam@email.com';

    WRITELN(Person_1._id);                      // 1
    WRITELN(Person_1._name);                    // Adam
    WRITELN(Person_1._email);                   // adam@email.com

    // initialise record using with
    WITH Person_2 do
    BEGIN
        _id := 2;
        _name := 'Bard';
        _email := 'bard@email.com';
    END;

    WRITELN(Person_2._id);                      // 2
    WRITELN(Person_2._name);                    // Bard
    WRITELN(Person_2._email);                   // bard@email.com
END.