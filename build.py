# Usage: pip install -r requirements.txt; python3 build.py (cloudflare pages)

# build script
import os
import re
import markdown
from natsort import natsorted
# syntax highlight
from bs4 import BeautifulSoup
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

FORMAT_MAP = {
    "py": "python",
    "c": "c",
    "cpp": "cpp",
    "pas": "pascal",
    "rb": "ruby",
    "rs": "rust",
    "pl": "prolog",
    "scala": "scala",
    "asm": "asm",
    "v": "verilog",
    "txt": "txt"
}
def syntax_highlight(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    code_blocks = soup.find_all("code")
    if code_blocks:
        for code_block in code_blocks:
            try:
                code_content = code_block.get_text()
                code_language = code_block.get('class')[0].split("-")[1]
                lexer = get_lexer_by_name(code_language, stripall=True)
                formatter = HtmlFormatter(linenos=False, cssclass="highlight")
                highlighted_code = highlight(code_content, lexer, formatter)
                code_block.parent.unwrap()
                code_block.replace_with(BeautifulSoup(highlighted_code, "html.parser"))
            except:
                pass
        html_content = str(soup)
    return html_content

# build paths map
paths = {}
postfix = (".asm", ".c", ".cc", ".cpp", ".pas", ".pl", ".py", ".rs", ".scala", ".v")
ignore = ("DRAFT", "TEST", "OLD", "_")
for root, dirs, files in os.walk("."):
    # for file in files
    for file in files:
        if file != "build.py" and file.endswith(postfix) and not (file.startswith(ignore)):
            try:
                _, language, category = root.split("/")
                if not language.startswith("_") and category != "_ignore":
                    if not language in paths.keys(): paths[language] = {}
                    if not category in paths[language].keys(): paths[language][category] = []
                    paths[language][category].append(file)
            except:
                pass

# sort
for language in paths.keys():
    for category in paths[language].keys():
        paths[language][category] = natsorted(paths[language][category], key=lambda item: item)

# create and write to file index.html
with open("index.html", "w+") as index:
    index.write("<meta charset='utf-8'>")
    index.write("<link rel='stylesheet' href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css' integrity='sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN' crossorigin='anonymous'>")
    index.write("<script src='https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js' integrity='sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+' crossorigin='anonymous'></script>")
    # styling
    index.write("""<style>
        @font-face {
            font-family: "Fira Mono"; src: local("Fira Mono Regular"), url("__fonts/FiraMono-Regular.ttf");
            font-weight: normal; font-style: normal;
        }
        @font-face {
            font-family: "Fira Mono"; src: local("Fira Mono Bold"), url("__fonts/FiraMono-Bold.ttf");
            font-weight: bold; font-style: normal;
        }
        body { font-size: 16px; font-family: "Fira Mono", monospace; }
        h1 { margin: 0.5rem, 0; }
        h1 a:first-child { margin-left: 1rem; }
        h2 { margin: 0.5rem, 0; }
        p { margin: 0; }
        .row .wrapper { padding: 0.5rem 0; }
        .row .wrapper p { margin-left: 1rem; }
        a { display: inline-block; cursor: pointer; margin-right: 1rem; text-underline-position: from-font; }
        a.dotted { text-decoration-style: dotted; }
        a.dotted:hover { color: #ff1f8f; text-decoration-style: solid; }
        pre { border: 2px solid black; border-radius: 0rem; font-size: 12px; padding: 0.5rem; white-space: break-spaces; line-break: anywhere; margin: 0; scroll: none; }
        pre::-webkit-scrollbar { width: 0; }
        hr { margin: 4px 0 !important; opacity: 1; border-color: black; border-width: 2px; }
        hr.muted { margin: 4px 0 !important; opacity: 1; border-color: #b4b4b4; border-width: 1px; }
        .wrapper { margin: 0 -4px; padding-bottom: 4px; }
        .wrapper .box { padding: 0 4px; }
        .float-right { float: right; }
        div.box.focus pre { border: 2px solid #ff1f8f; }
        /* code highlight */
        .highlight .k { color: #ff1f8f !important; }
        .highlight .n { color: black !important; }
        .highlight .kn { color: black !important; }
        .highlight .s1, .highlight .si { color: #ff9800 !important; }
        .highlight .c1, .highlight .cm { color: #b4b4b4 !important; }
        .highlight .mi { color: black !important; }
        .highlight .nf, .highlight .nb { font-weight: bold; }
        .highlight .nc { color: black !important; font-weight: bold; }
    </style>""")
    # javascript
    index.write("""<script>
        document.addEventListener("DOMContentLoaded", function() {
            // add focus on link click
            document.querySelectorAll("a").forEach(function(anchor) {
                anchor.addEventListener("click", function() {
                    var anchor_name = anchor.getAttribute("href").replace("#", "");
                    var div = document.querySelector("a[name='" + anchor_name + "']").closest("div");
                    if (div) {
                        div.classList.add("focus");
                        // setTimeout(function() { div.classList.remove("focus"); }, 2000);
                    }
                });
            });
            // remove focus
            document.querySelectorAll("div.box").forEach(function(box) {
                box.addEventListener("click", function() {
                    document.querySelectorAll("div.box").forEach(function(box) { box.classList.remove("focus"); });
                });
            });
        });
    </script>""")
    current_lang = ""
    current_category = ""
    # container
    index.write("<div class='container-fluid mb-1'>")
    index.write("<a name='top'></a>")
    # link to languages
    index.write("<div class='row'>")
    index.write("<div class='col'>")
    index.write("<a class='dotted' data-bs-toggle='collapse' data-bs-target='#collapseIndex' aria-expanded='false' aria-controls='collapseIndex'>&#172;</a>")
    for language in paths.keys(): index.write(f"<a class='dotted' href='#{language}'>{language}</a>")
    # github
    index.write("<a class='float-right' href='https://github.com/mxsjoberg/code'>Github</a>")
    index.write("</div>") # col
    index.write("</div>") # row
    # collapse index with all languages, categories, and files
    index.write("<div class='row'>")
    index.write("<div class='col' style='column-count:4;'>")
    index.write("<div class='collapse' id='collapseIndex'>")
    for language in paths.keys():
        for category in paths[language].keys():
            index.write("<div class='row'><hr class='muted'></div>")
            index.write(f"{language}")
            index.write(f"<a class='dotted' style='margin-left:12px;' href='#{language}-{category}'>{category}</a><br>")
            for file in paths[language][category]:
                index.write(f"<a class='dotted' href='#{file.replace('.', '-')}'>{file}</a><br>")
            index.write("<br>")
    index.write("</div>") # collapse
    index.write("</div>") # col
    index.write("</div>") # row
    # start of main page
    for language in paths.keys():
        index.write("<div class='row'><hr></div>")
        index.write("<div class='row'>")
        index.write("<div class='col-12'>")
        # current language
        if current_lang != language:
            current_lang = language
            current_category = ""
            # write language
            index.write(f"<a name='{language}'></a>")
            index.write(f"<h1>{language}")
            for category in paths[language].keys(): index.write(f"<a class='dotted' href='#{language}-{category}'>{category}</a>")
            index.write("<a class='dotted float-right' href='#top'>^</a>")
            index.write("</h1>")
        # for each category
        for category in paths[language].keys():
            # current category
            if current_category != category:
                current_category = category
                # start new category
                index.write(f"<a name='{language}-{category}'></a>")
                index.write(f"<h2>{category}")
                index.write("<a class='dotted float-right' href='#top'>^</a>")
                index.write("</h2>")
                index.write("<p>")
                for file in paths[language][category]:
                    # write link to file
                    index.write(f"<a class='dotted' href='#{file.replace('.', '-')}'>{file}</a>")
                index.write("</p>")
            index.write("<div class='container-fluid p-0'>")
            index.write("<div class='row wrapper'>")
            # for each file in category
            for file in paths[language][category]:
                # index.write(f"<div class='col-12 col-md-6 col-xl-4 box'>")
                index.write(f"<div class='col-12 box'>")
                # write link to raw file
                index.write(f"<a class='dotted' href='#{file.replace('.', '-')}'>{file}</a>")
                index.write(f"[<a href='https://github.com/mxsjoberg/code/blob/master/{language}/{category}/{file}' name='{file.replace('.', '-')}' class='m-0'>github</a>]")
                # write content in file
                file_content = open(f"{language}/{category}/{file}").read()
                file_content_as_markdown = f"```{FORMAT_MAP[file.split('.')[1]]}\n{file_content}\n```\n" # escape special characters
                html_content = markdown.markdown(file_content_as_markdown, extensions=["fenced_code"])
                index.write(syntax_highlight(html_content))
                index.write("</div>") # col
            index.write("</div>") # row
            index.write("</div>") # container
        index.write("</div>") # col
        index.write("</div>") # row
    index.write("</div>") # container
