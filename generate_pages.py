import os

output_dir = r"f:\COVANA\Heranba\wireframes\pages"
if not os.path.exists(output_dir): os.makedirs(output_dir)

# -----------------------------------------------------------------------
# PAGE ARCHITECTURE (matches PDF sitemap)
# - Single pages: all sections render on ONE page as scrollable sections
# - Hub/Multi pages: the hub page + each item is its own .html file
# -----------------------------------------------------------------------

pages_config = {
    # ── SINGLE PAGES (no child pages in nav) ───────────────────────────
    "home": [
        "Hero Showcase", "Introduction to Heranba", "Key Features",
        "Latest Updates", "Contact Us", "Downloads", "Blogs & Articles"
    ],

    # Media & Resources = ONE combined page with its own sections
    "media_resources": [
        "Video Gallery", "Photo Gallery", "Events Calendar", 
        "News & Updates", "Press Releases", "Media Contact",
        "Blogs & Articles", "Downloads"
    ],

    "contact": [
        "Get in Touch", "Corporate Office", "Regional Offices",
        "Dealer Enquiry", "Customer Support", "Investor Contact"
    ],

    "investor_relations": [
        "Financials Overview", "Disclosures & Announcements", 
        "Corporate Governance", "Stock Information"
    ],

    "careers": [
        "Life at Heranba", "Why Heranba", "Open Positions", 
        "Apply for a Job", "Employee Stories", "Contact HR"
    ],

    # ── HUB PAGES (each child below is its own .html file) ─────────────

    # Products hub
    "products": ["Products Overview", "Formulations", "Intermediates", "Technicals", "Explore Brands"],

    # Products sub-pages
    "formulations":  ["Formulations Overview", "Crop Nutrition", "Fungicides", "Herbicides", "Insecticides", "Public Health"],
    "intermediates": ["Intermediates Overview", "Showcase", "Technical Specs", "Inquiry"],
    "technicals":    ["Technicals Overview",    "Showcase", "Technical Specs", "Inquiry"],
    "crop_nutrition": ["Crop Nutrition Hub", "Bio Stimulant", "Bio Fertilizer", "Micro Nutrient Fertilizer", "Water Soluble", "PGR"],
    "bio_stimulant":           ["Bio Stimulants",      "Intro", "Products", "Usage"],
    "bio_fertilizer":          ["Bio Fertilizer",      "Intro", "Products", "Usage"],
    "micro_nutrient_fertilizer": ["Micro Nutrients",   "Intro", "Products", "Usage"],
    "water_soluble_fertilizer": ["Water Soluble Fert.", "Intro", "Products", "Usage"],
    "pgr":         ["PGR Expert Guide",   "About", "Products", "Benefits", "Usage", "FAQs", "Contact"],
    "fungicides":  ["Fungicide Range",    "Showcases", "Innovations", "Inquiry"],
    "herbicides":  ["Herbicide Range",    "Showcases", "Innovations", "Inquiry"],
    "insecticides": ["Insecticide Range", "Showcases", "Innovations", "Inquiry"],
    "public_health": ["Public Health Solutions", "Solutions", "Measures", "Learn"],

    # Farmer Corner hub
    "farmer_corner": ["Farmer Corner Hub", "Market Information", "Farmer Portal", "Crop Calendars", "Pest & Diseases Guide", "Crop Advisory"],

    # Market Information hub
    "market_information": ["Market Overview", "Mandi Prices", "Weather Forecasts", "Government Schemes", "Case Studies"],
    "mandi_prices": ["Mandi Prices Update", "Price Trends", "Market Arrivals"],
    "weather_forecasts": ["Weather Forecast", "Local Updates", "Agriculture Tips"],
    "government_schemes": ["Govt Schemes Hub", "Financial Assistance", "Subsidies"],
    "case_studies": ["Success Implementations", "Farmer Stories", "Outcomes"],

    # Farmer Portal hub (7 sub-pages)
    "farmer_portal": ["Portal Hub", "Contests", "Farmer Programs", "Recognition Awards", "Farmer Community", "Farmer Testimonials", "Success Stories", "Member Log-in"],
    "contests": ["Farmer Contests", "Current Contests", "Rules", "Prizes"],
    "farmer_programs": ["Farmer Programs", "Training", "Development", "Support"],
    "recognition_awards": ["Farmer Awards", "Nomination", "Winners"],
    "heranba_farmer_community": ["Community Hub", "Forums", "Networking", "Events"],
    "farmer_testimonials": ["Farmer Testimonials", "Quotes", "Videos"],
    "success_stories": ["Success Stories", "Transformational Journeys", "Impact"],

    # Advisory sub-pages
    "crop_advisory":          ["Crop Advisory Hub", "Expert Consultations", "Soil Health"],
    "pest_diseases_guide":    ["Pest & Diseases Guide", "Identification", "Management"],
    "crop_calendars":         ["Crop Calendars", "Seasonal Schedules", "Harvesting"],

    # About Us hub
    "about_us": [
        "Our Legacy", "Our Story", "Corporate Film", "Global Presence",
        "Awards & Recognitions", "News and Articles"
    ],

    # About Us sub-pages
    "management_team": ["Meet our key people", "Our management philosophy", "Our team members", "Contact Management"],
    "news_and_articles": ["Recent News", "Industry Articles", "Write for us", "Subscribe for updates"],
    "facilities":      ["Manufacturing Excellence", "Overview", "Manufacturing Facilities", "R&D", "Quality Control", "Future Scope"],
    "life_at_heranba": ["Life at Heranba", "Culture", "Events", "Employee Stories"],
    "why_heranba":     ["Why Heranba", "Vision", "Values", "Achievements"],

    # Knowledge Centre hub
    "knowledge_centre": ["Knowledge Hub", "Downloads", "Expert Articles", "Video Library", "Training Materials"],

    # Knowledge Centre sub-pages
    "downloads":          ["Available Downloads", "Brochures", "Catalogs", "Product Data Sheets"],
    "expert_articles":    ["Expert Insights",     "Scientific Papers", "Agronomy Tips", "Case Studies"],
    "video_library":      ["Video Resources",     "Product Demos", "Corporate Videos", "Training Clips"],
    "training_materials": ["Training Hub",        "Safety Guides", "Application Manuals", "Workshops"],
}

def get_link_for_section(section_name):
    normalized = section_name.lower().replace(" ", "_").replace("&", "and").replace("-", "_")
    if normalized in pages_config: return f"{normalized}.html"
    return f"#{normalized}"

def get_component_html(name, index, page_id):
    lower_name = name.lower()
    anchor_id = name.lower().replace(" ", "_").replace("&", "and").replace("-", "_")
    
    # 2. PRODUCT / ITEM SHOWCASE (Grids)
    if any(x in lower_name for x in ["product", "range", "showcase", "gallery", "archive", "list", "available", "categories"]):
        cols = 3 if index % 2 == 0 else 4
        cards = "".join([f'<div class="card"><div class="card-img"></div><div class="card-title">Product/Item {i+1}</div><div class="card-desc">Feature summary for {name} content.</div></div>' for i in range(cols)])
        return f"""
        <div class="section" id="{anchor_id}">
            <div class="section-header"><h2 class="section-title">{name}</h2></div>
            <div class="grid-3" style="grid-template-columns: repeat({cols}, 1fr);">
                {cards}
            </div>
        </div>
        """

    # 3. SPLIT CONTENT (Alternating layouts)
    if any(x in lower_name for x in ["about", "story", "legacy", "philosophy", "overview", "intro", "guide", "expert", "innovation", "bio", "stimulant", "fertilizer", "pgr", "fungicide", "herbicide", "insecticide", "solutions"]):
        reverse = "split-reverse" if index % 2 != 0 else ""
        return f"""
        <div class="section" id="{anchor_id}">
            <div class="split-content {reverse}">
                <div class="split-text">
                    <h2 class="section-title">{name}</h2>
                    <p style="margin-bottom: 20px; line-height: 1.6; font-size: 18px;">Detailed insights into {name}. This section uses a split layout to provide a balanced mix of visual and textual information, ideal for storytelling or technical explanations.</p>
                    <ul style="margin-bottom: 25px; padding-left: 20px;">
                        <li style="margin-bottom: 10px;">Key Feature One</li>
                        <li style="margin-bottom: 10px;">Benefit for the user/farmer</li>
                        <li style="margin-bottom: 10px;">Technical Specification</li>
                    </ul>
                    <div class="btn">Read Details</div>
                </div>
                <div class="split-media"></div>
            </div>
        </div>
        """

    # 4. DATA / TABLES / LISTS
    if any(x in lower_name for x in ["price", "mandi", "weather", "filings", "results", "reports", "statutory", "dividend", "calendar"]):
        return f"""
        <div class="section" id="{anchor_id}">
            <div class="section-header"><h2 class="section-title">{name}</h2></div>
            <div style="border: 2px solid #000; padding: 20px;">
                <div style="display: flex; justify-content: space-between; padding: 15px; border-bottom: 2px solid #000; font-weight: 800; text-transform: uppercase;">
                    <span>Metric / Item</span><span>Value / Date</span><span>Status</span>
                </div>
                {"".join([f'<div style="display: flex; justify-content: space-between; padding: 15px; border-bottom: 1px solid #eee;"><span>Example Entry {i+1}</span><span>Row Data</span><span>[Icon]</span></div>' for i in range(5)])}
            </div>
        </div>
        """

    # 5. TEAM / PROFILES
    if any(x in lower_name for x in ["team", "leadership", "management", "board", "directors", "people"]):
        return f"""
        <div class="section" id="{anchor_id}">
            <div class="section-header"><h2 class="section-title">{name}</h2></div>
            <div class="grid-3">
                {"".join([f'<div class="card" style="text-align: center;"><div class="card-img" style="aspect-ratio: 1/1; border-radius: 50%;"></div><div class="card-title">Executive Name {i+1}</div><div class="card-desc">Designation & Brief Bio</div></div>' for i in range(3)])}
            </div>
        </div>
        """

    # 6. FORMS / CONTACT
    if any(x in lower_name for x in ["contact", "enquiry", "apply", "join", "subscribe", "nomination", "request"]):
        return f"""
        <div class="section" id="{anchor_id}" style="background: #f9f9f9;">
            <div style="max-width: 800px; margin: 0 auto; text-align: center;">
                <div class="section-header"><h2 class="section-title">{name}</h2></div>
                <p style="margin-bottom: 40px;">Please fill out the form below for {name}.</p>
                <div class="wireframe-form" style="margin: 0 auto; text-align: left;">
                    <div class="f-row"></div><div class="f-row"></div><div class="f-area"></div>
                    <div class="btn" style="width: 100%; text-align: center;">Submit {name}</div>
                </div>
            </div>
        </div>
        """

    # 7. FAQ / ACCORDION
    if any(x in lower_name for x in ["faq", "question", "rules", "guidelines"]):
        return f"""
        <div class="section" id="{anchor_id}">
            <div class="section-header"><h2 class="section-title">{name}</h2></div>
            {"".join([f'<div style="padding: 20px; border: 1px solid #000; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center; font-weight: 600;"><span>Question {i+1} for {name}?</span><span>+</span></div>' for i in range(4)])}
        </div>
        """

    # 8. STATS / HIGHLIGHTS
    if any(x in lower_name for x in ["highlight", "overview", "statistics", "at a glance", "financial", "performance"]):
        return f"""
        <div class="section" id="{anchor_id}">
            <div class="section-header"><h2 class="section-title">{name}</h2></div>
            <div class="stats-grid">
                <div class="stat-item"><div class="stat-num">Data Pt 1</div><div class="stat-label">Metric Label</div></div>
                <div class="stat-item"><div class="stat-num">Data Pt 2</div><div class="stat-label">Metric Label</div></div>
                <div class="stat-item"><div class="stat-num">Data Pt 3</div><div class="stat-label">Metric Label</div></div>
                <div class="stat-item"><div class="stat-num">Data Pt 4</div><div class="stat-label">Metric Label</div></div>
            </div>
        </div>
        """

    # 9. TIMELINE / STEPS
    if any(x in lower_name for x in ["process", "module", "step", "history", "milestones"]):
        return f"""
        <div class="section" id="{anchor_id}">
            <div class="section-header"><h2 class="section-title">{name}</h2></div>
            <div style="display: flex; gap: 20px;">
                {"".join([f'<div style="flex: 1; padding: 20px; border: 1px solid #000; position: relative;"><div style="width: 30px; height: 30px; background: #000; color: #fff; display: flex; align-items: center; justify-content: center; font-weight: bold; margin-bottom: 15px;">{i+1}</div><h4>Phase {i+1}</h4><p style="font-size: 13px; opacity: 0.7;">Description of this phase in the {name}.</p></div>' for i in range(4)])}
            </div>
        </div>
        """

    # DEFAULT
    return f"""
    <div class="section" id="{anchor_id}">
        <div class="section-header"><h2 class="section-title">{name}</h2></div>
        <div class="grid-3">
            <div class="card"><div class="card-img"></div><div class="card-title">Default Item</div><div class="card-desc">Generic description for {name}.</div></div>
            <div class="card"><div class="card-img"></div><div class="card-title">Default Item</div><div class="card-desc">Generic description for {name}.</div></div>
            <div class="card"><div class="card-img"></div><div class="card-title">Default Item</div><div class="card-desc">Generic description for {name}.</div></div>
        </div>
    </div>
    """

header_html = """
<header>
  <div class="logo-box">HERANBA</div>
  <nav>
    <div class="nav-item"><a href="home.html">Home</a></div>
    
    <div class="nav-item">
      <a href="products.html">Products <span class="caret">&#9660;</span></a>
      <div class="dropdown">
        <div class="dropdown-col">
          <div class="dropdown-col-title">Formulations</div>
          <a href="fungicides.html">Fungicides</a>
          <a href="herbicides.html">Herbicides</a>
          <a href="insecticides.html">Insecticides</a>
          <a href="public_health.html">Public Health</a>
        </div>
        <div class="dropdown-col">
          <div class="dropdown-col-title">Crop Nutrition</div>
          <a href="bio_stimulant.html">Bio Stimulant</a>
          <a href="bio_fertilizer.html">Bio Fertilizer</a>
          <a href="micro_nutrient_fertilizer.html">Micro Nutrient Fertilizer</a>
          <a href="water_soluble_fertilizer.html">Water Soluble</a>
            <a href="pgr.html">PGR</a>
        </div>
        <div class="dropdown-col">
          <div class="dropdown-col-title">Core Manufacturing</div>
          <a href="intermediates.html">Intermediates</a>
          <a href="technicals.html">Technicals</a>
        </div>
      </div>
    </div>

    <div class="nav-item">
      <a href="farmer_corner.html">Farmer Corner <span class="caret">&#9660;</span></a>
      <div class="dropdown">
        <div class="dropdown-col">
          <div class="dropdown-col-title">Market Info</div>
          <a href="mandi_prices.html">Mandi Prices</a>
          <a href="weather_forecasts.html">Weather Forecasts</a>
          <a href="government_schemes.html">Govt Schemes</a>
          <a href="case_studies.html">Case Studies</a>
        </div>
        <div class="dropdown-col">
          <div class="dropdown-col-title">Farmer Portal</div>
          <a href="contests.html">Contests</a>
          <a href="farmer_programs.html">Programs</a>
          <a href="recognition_awards.html">Awards</a>
          <a href="heranba_farmer_community.html">Community</a>
          <a href="farmer_testimonials.html">Testimonials</a>
          <a href="success_stories.html">Success Stories</a>
        </div>
        <div class="dropdown-col">
          <div class="dropdown-col-title">Advisory</div>
          <a href="crop_advisory.html">Crop Advisory</a>
          <a href="pest_diseases_guide.html">Pest &amp; Diseases</a>
          <a href="crop_calendars.html">Crop Calendars</a>
        </div>
      </div>
    </div>

    <div class="nav-item"><a href="facilities.html">Facilities</a></div>
    
    <div class="nav-item">
      <a href="knowledge_centre.html">Knowledge <span class="caret">&#9660;</span></a>
      <div class="dropdown">
        <div class="dropdown-col">
          <a href="downloads.html">Downloads</a>
          <a href="expert_articles.html">Expert Articles</a>
          <a href="video_library.html">Video Library</a>
          <a href="training_materials.html">Training Materials</a>
        </div>
      </div>
    </div>

    <div class="nav-item"><a href="investor_relations.html">Investors</a></div>

    <div class="nav-item"><a href="media_resources.html">Media &amp; Resources</a></div>

    <div class="nav-item">
      <a href="about_us.html">About <span class="caret">&#9660;</span></a>
      <div class="dropdown">
        <div class="dropdown-col">
          <a href="about_us.html">Our Story</a>
          <a href="management_team.html">Management</a>
          <a href="news_and_articles.html">News &amp; Articles</a>
        </div>
      </div>
    </div>

    <div class="nav-item"><a href="careers.html">Careers</a></div>

    <div class="nav-item"><a href="contact.html">Contact</a></div>
  </nav>
</header>
"""
footer_html = """
<footer class="footer-wireframe">
    <div class="footer-main-grid">
        <!-- Section: Newsletter -->
        <div class="footer-section-box newsletter-col">
            <div>
                <span class="wireframe-label">Newsletter Component</span>
                <div class="text-placeholder ph-h2"></div>
                <div class="text-placeholder ph-h2" style="width: 85%;"></div>
            </div>
            <div>
                <div class="subscribe-box">
                    <div class="text-placeholder ph-link" style="margin: 10px; width: 120px; background: transparent; border: 1px dashed #ccc;"></div>
                    <button>SUBSCRIBE</button>
                </div>
                <div class="text-placeholder ph-p short"></div>
            </div>
        </div>

        <!-- Section: Contact Info -->
        <div class="footer-section-box contact-col">
            <div class="location-section">
                <span class="wireframe-label">Location Block</span>
                <div class="text-placeholder ph-h3"></div>
                <div class="text-placeholder ph-p"></div>
                <div class="text-placeholder ph-p medium"></div>
            </div>
            <div class="hello-section">
                <span class="wireframe-label">Contact Block</span>
                <div class="text-placeholder ph-h3"></div>
                <div class="text-placeholder ph-h1" style="width: 100%; margin-top: 10px;"></div>
            </div>
        </div>

        <!-- Section: Links -->
        <div class="footer-section-box links-col">
            <div>
                <span class="wireframe-label">Navigation Links</span>
                <div class="text-placeholder ph-h3"></div>
                <div class="links-grid">
                    <div class="link-item"><div class="text-placeholder ph-link"></div></div>
                    <div class="link-item"><div class="text-placeholder ph-link" style="width: 60px;"></div></div>
                    <div class="link-item"><div class="text-placeholder ph-link" style="width: 90px;"></div></div>
                    <div class="link-item"><div class="text-placeholder ph-link" style="width: 70px;"></div></div>
                    <div class="link-item"><div class="text-placeholder ph-link" style="width: 50px;"></div></div>
                    <div class="link-item"><div class="text-placeholder ph-link" style="width: 85px;"></div></div>
                    <div class="link-item"><div class="text-placeholder ph-link" style="width: 75px;"></div></div>
                    <div class="link-item"><div class="text-placeholder ph-link" style="width: 65px;"></div></div>
                </div>
            </div>
            <div class="social-links">
                <span class="wireframe-label">Social Media</span>
                <div class="social-icons-row">
                    <div class="social-circle"></div>
                    <div class="social-circle"></div>
                    <div class="social-circle"></div>
                    <div class="social-circle"></div>
                    <div class="social-circle"></div>
                </div>
            </div>
        </div>
    </div>
    <!-- Bottom Bar -->
    <div class="footer-bottom-bar">
        <div class="brand-logo">
            <div class="logo-icon"></div>
            <div class="text-placeholder ph-h3" style="width: 120px; margin-bottom: 0;"></div>
        </div>
        <div class="text-placeholder ph-p medium" style="width: 300px; margin-bottom: 0;"></div>
    </div>
</footer>
"""

base_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PAGE_TITLE - Heranba Wireframe</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <div class="wireframe-container">
        HEADER
        <div class="hero-banner"><div class="hero-box"><h1 style="font-size: 56px;">PAGE_TITLE</h1><p style="margin-top:20px; opacity:0.6;">Sitemap Blueprint v2</p></div></div>
        <div class="section" style="background:#f0f0f0; padding: 20px 60px; border-bottom: 2px solid #000;"><div style="display: flex; flex-wrap: wrap; gap: 10px;">SUBNAV_LINKS</div></div>
        BODY_CONTENT
        FOOTER
    </div>
</body>
</html>
"""

for pid, sections in pages_config.items():
    display_title = pid.replace("_", " ").title() if pid != "pgr" else "PGR"
    body_content = "".join([get_component_html(s, i, pid) for i, s in enumerate(sections)])
    subnav_links = "".join([f'<a href="{get_link_for_section(s)}" class="btn" style="background:#fff; border:1px solid #000; color:#000; font-size:11px; padding: 10px 15px;">{s}</a>' for s in sections])
    final_html = base_html.replace("PAGE_TITLE", display_title).replace("HEADER", header_html).replace("SUBNAV_LINKS", subnav_links).replace("BODY_CONTENT", body_content).replace("FOOTER", footer_html)
    with open(os.path.join(output_dir, f"{pid}.html"), "w", encoding="utf-8") as f: f.write(final_html)

print(f"Generated 44 HIGH-VARIETY wireframe pages with unique section types.")
