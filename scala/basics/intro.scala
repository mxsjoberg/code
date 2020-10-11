/*
	Scala is a general-purpose, functional programming language developed by Martin Odersky in 2004.

	https://en.wikipedia.org/wiki/Scala_(programming_language)
*/

object Main {
    // do something

    def main(args: Array[String]) {
        // do something
    }
}

// compile and run from command-line:
// 	$ scalac <filename>.scala
// 	$ scala <filename>

// compile and run from sublime text
{
    "cmd": ["scala", "$file"],
    "path": "$PATH:/usr/local/bin",
    "file_regex": "^(.+):(\\d+): .+: (.+)",
    "selector": "source.scala"
}