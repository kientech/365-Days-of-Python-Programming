# Coding With Kien - 365 Days of Python Programming
# Intermediate - Day 15

# Markdown to HTML Converter
# This script requires the 'markdown' library:
# pip install markdown

import markdown
import os

def convert_md_to_html(input_file, output_file):
    """
    Converts a Markdown file to an HTML file.
    """
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        return

    with open(input_file, 'r') as f:
        md_text = f.read()

    html = markdown.markdown(md_text)

    with open(output_file, 'w') as f:
        f.write(html)

    print(f"Successfully converted '{input_file}' to '{output_file}'")

# --- Example Usage ---
# Create a dummy markdown file
md_content = """
# My Awesome Document

This is a paragraph. *This text is italic.* **This text is bold.**

- List item 1
- List item 2

Check out [this link](https://www.python.org).
"""
input_md_file = "sample.md"
output_html_file = "sample.html"

with open(input_md_file, "w") as f:
    f.write(md_content)

# Perform the conversion
convert_md_to_html(input_md_file, output_html_file)

# You can now open 'sample.html' in your browser to see the result. 