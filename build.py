# build script to generate static website

import os

readme = open("README.md", "w+")

# create and write to file index.html
with open("index.html", "w+") as index:
    # index.write("<style>div {column-count: 5} p {margin: 0}</style>")
    index.write("<style>body { font-family: 'Lucida Console', monospace } p { margin: 0; }</style>")
    readme.write("# Programming\n\n")
    current_lang = ""
    current_category = ""
    # for folder in root not www
    for root, dirs, files in os.walk("."):
        # for file in files
        for file in files:
            if file != "build.py" and file.endswith((".asm", ".c", ".cc", ".cpp", ".pas", ".pl", ".py", ".rs", ".scala", ".v")) and not file.startswith(("DRAFT", "TEST", "OLD")):
                _, language, category = root.split("/")
                # programming language
                if current_lang != language:
                    current_lang = language
                    if not current_lang == "":
                        index.write("</div>")
                        readme.write("\n")
                    index.write("<h1>" + language + "</h1>")
                    index.write("<div>")
                    readme.write("## " + language + "\n\n")
                # category
                if current_category != category:
                    current_category = category
                    if not current_category == "":
                        index.write("</div>")
                        readme.write("\n")
                    index.write("<h2>" + category + "</h2>")
                    index.write("<div>")
                    readme.write("### " + category + "\n\n")
                # write link to file
                index.write("<p><a href='" + root + "/" + file + "'>" + file + "</a></p>")
                readme.write("* [" + file.split(".")[0] + "](" + root.replace(".", "https://github.com/mixmaester/programming/blob/master") + "/" + file + ")\n")

    index.write("</div>")

readme.close()