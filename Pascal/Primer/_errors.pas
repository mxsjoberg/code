// 2020-02
program Errors;
uses sysutils;

type
    TestException = class(Exception);

begin
    try
        if 1 = 2 then
        begin
            raise TestException.Create('something is wrong');
        end;
    except
        begin
        end;
    end;
end.