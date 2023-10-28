/*
    Scala is a general-purpose, functional programming language developed by Martin Odersky in 2004.

    https://en.wikipedia.org/wiki/Scala_(programming_language)
*/

object Intro {
    // Unit is same as void in Java
    def main(args: Array[String]): Unit = {
        // do something
        println("hello scala");
    }
}

/*
    compile and run from command-line:
        $ scalac <filename>.scala
        $ scala <filename>

    build-system (sublime text):
        {
            "cmd": ["scala", "$file"],
            "path": "$PATH:/usr/local/bin",
            "file_regex": "^(.+):(\\d+): .+: (.+)",
            "selector": "source.scala"
        }
*/