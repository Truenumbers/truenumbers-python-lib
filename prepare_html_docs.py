import os
import re

def cleanup_html(html: str) -> str:
    """
    - Remove any <td class="extra">...</td> elements that pydoc puts
      in the header of generated HTML files.
    - Rewrite the src index link from "src.html" to "/" for nicer URLs.
    """
    html = re.sub(r'<td class="extra">.*?</td>', "", html, flags=re.DOTALL)
    html = html.replace('href="src.html"', 'href="/"')
    return html


for file in os.listdir("docs"):
    if file.endswith(".html"):
        with open(os.path.join("docs", file), "r", encoding="utf-8") as f:
            html = f.read()

        html = cleanup_html(html)

        with open(
            os.path.join("docs", file), "w", encoding="utf-8"
        ) as f:
            f.write(html)


