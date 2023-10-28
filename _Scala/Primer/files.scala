import scala.io.Source
import java.io._

// read from file
val file = Source.fromFile("path/to/file")

for (line <- file.getLines) {
    // do something
}
file.close

// write to file
val file = new File("path/to/file.txt")
val buffer = new BufferedWriter(new FileWriter(file))

buffer.write("Text.")
buffer.close