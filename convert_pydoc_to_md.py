from html_to_markdown import convert
import os

for file in os.listdir("docs"):
    if file.endswith(".html"):
        with open(os.path.join("docs", file), "r") as f:
            html = f.read()
        markdown = convert(html)
        with open(os.path.join("docs", file.replace(".html", ".md")), "w") as f:
            f.write(markdown)
        os.remove(os.path.join("docs", file))

