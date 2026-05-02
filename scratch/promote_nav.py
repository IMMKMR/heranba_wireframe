import os
import re

directory = r'f:\COVANA\Heranba\wireframes\pages'

# Regex to match the Formulations nav-item block (the one we just created in previous turns)
pattern = re.compile(
    r'(<div class="nav-item">\s*<a href="products\.html">\s*Formulations\s*<span class="caret">&#9660;</span></a>\s*<div class="dropdown">).*?(</div>\s*</div>)',
    re.DOTALL | re.IGNORECASE
)

new_nav_item = r'''<div class="nav-item">
            <a href="products.html">Products <span class="caret">&#9660;</span></a>
            <div class="dropdown">
              <div class="dropdown-col" style="min-width: 200px;">
                <div class="dropdown-col-title">Product Categories</div>
                <div class="has-submenu">
                  <a href="formulations.html">Formulations</a>
                  <div class="submenu">
                    <div class="has-submenu">
                      <a href="crop_nutrition.html">Crop Nutrition</a>
                      <div class="submenu">
                        <a href="bio_stimulant.html">Bio Stimulant</a>
                        <a href="bio_fertilizer.html">Bio Fertilizer</a>
                        <a href="micro_nutrient_fertilizer.html">Micro Nutrient Fertilizer</a>
                        <a href="water_soluble_fertilizer.html">Water Soluble</a>
                        <a href="pgr.html">PGR</a>
                      </div>
                    </div>
                    <a href="fungicides.html">Fungicides</a>
                    <a href="herbicides.html">Herbicides</a>
                    <a href="insecticides.html">Insecticides</a>
                    <a href="public_health.html">Public Health</a>
                  </div>
                </div>
                <a href="intermediates.html">Intermediates</a>
                <a href="technicals.html">Technicals</a>
              </div>
            </div>
          </div>'''

for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = pattern.sub(new_nav_item, content)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
