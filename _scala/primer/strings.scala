val string: String = "proton neutron"

string.charAt(0)                                        // p
string.slice(0,4)                                       // prot

// using length
string.length                                           // 14
string.substring(0, string.length)                      // proton neutron
string.substring(string.length - 4, string.length)      // tron

// built-ins
string.capitalize                                       // Proton neutron
string.toUpperCase                                      // PROTON NEUTRON
string.toLowerCase                                      // proton neutron

// counting and finding in text
string.count(_ == 'p')                                  // 1
string.indexOf("t")                                     // 3

// remove whitespace from string
val spacedstring: String = "    some text    "
spacedstring.trim                                       // some text