// 2021-05
program DateAndTime;
uses sysutils;

begin
    // time
    writeln(TimeToStr(Now));
    // 00:15:17

    // date
    writeln(DateToStr(Now));
    // 26-5-21

    // increment month
    writeln(DateToStr(IncMonth(Now)));
    // 26-6-21
end.