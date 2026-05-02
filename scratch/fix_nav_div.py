import os
import re

directory = r'f:\COVANA\Heranba\wireframes\pages'

# Regex to find the Products nav-item that has one too many </div> tags
# We look for the specific structure I created, which ends with </div> (nav-item)
# but might have an extra one left over from the previous regex mistake.

pattern = re.compile(
    r'(<div class="nav-item">\s*<a href="products\.html">Products <span class="caret">&#9660;</span></a>.*?</div>\s*</div>\s*</div>)\s*</div>',
    re.DOTALL | re.IGNORECASE
)

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # We only apply the fix if we find the pattern
        new_content = pattern.sub(r'\1', content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed {filename}")
