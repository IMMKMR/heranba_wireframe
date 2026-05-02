import os
import re

directory = r'f:\COVANA\Heranba\wireframes\pages'

# Regex to match the entire Formulations nav-item block
# We use a non-greedy match for the dropdown content
pattern = re.compile(
    r'(<div class="nav-item">\s*<a href="products\.html">Formulations <span class="caret">&#9660;</span></a>\s*<div class="dropdown">).*?(</div>\s*</div>)',
    re.DOTALL | re.IGNORECASE
)

new_dropdown_content = r'''\1
              <div class="dropdown-col">
                <div class="dropdown-col-title">Crop Nutrition</div>
                <a href="bio_stimulant.html">Bio Stimulant</a>
                <a href="bio_fertilizer.html">Bio Fertilizer</a>
                <a href="micro_nutrient_fertilizer.html">Micro Nutrient Fertilizer</a>
                <a href="water_soluble_fertilizer.html">Water Soluble</a>
                <a href="pgr.html">PGR</a>
              </div>
              <div class="dropdown-col">
                <div class="dropdown-col-title">Formulations</div>
                <a href="fungicides.html">Fungicides</a>
                <a href="herbicides.html">Herbicides</a>
                <a href="insecticides.html">Insecticides</a>
                <a href="public_health.html">Public Health</a>
              </div>
            \2'''

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = pattern.sub(new_dropdown_content, content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
