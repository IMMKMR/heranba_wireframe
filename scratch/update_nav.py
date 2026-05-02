import os
import re

directory = r'f:\COVANA\Heranba\wireframes\pages'

# Even more flexible regex to handle any whitespace within the tags
old_nav_pattern = re.compile(r'<a\s+href="products\.html"[\s>]*Products\s*<span\s+class="caret"[\s>]*&#9660;\s*</span\s*>\s*</a\s*>', re.IGNORECASE | re.MULTILINE)
new_nav_replacement = '<a href="products.html">Formulations <span class="caret">&#9660;</span></a>'

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = old_nav_pattern.sub(new_nav_replacement, content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
