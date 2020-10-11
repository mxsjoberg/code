import java.util.Calendar
import java.text.SimpleDateFormat

val now = Calendar.getInstance.getTime
// Sun Jun 17 19:18:49 CEST 2018

val year = new SimpleDateFormat("yyyy")
val month = new SimpleDateFormat("M")
val day = new SimpleDateFormat("d")
val hour = new SimpleDateFormat("H")
val minute = new SimpleDateFormat("m")

year.format(now)                            // 2018
month.format(now)                           // 6
day.format(now)                             // 17
hour.format(now)                            // 19
minute.format(now)                          // 18