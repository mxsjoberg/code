PROGRAM date_and_time;
USES sysutils;
BEGIN
    // time
    WRITELN(TimeToStr(Now));
    // 00:15:17

    // date
    WRITELN(DateToStr(Now));
    // 26-5-21

    // increment month
    WRITELN(DateToStr(IncMonth(Now)));
    // 26-6-21
END.