import os

output_dir = r"f:\COVANA\Heranba\wireframes\pages"
if not os.path.exists(output_dir): os.makedirs(output_dir)

pages_config = {
    "home": ["Hero Showcase", "Introduction to Heranba", "Our key features", "Explore our latest updates", "Contact us for more information", "Downloads", "Blogs and Articles"],
    "farmer_corner": ["Farmer Corner Hub", "Crop Advisory", "Pest & Diseases Guide", "Crop Calendars", "Farmer Portal", "Join Heranba Farmer Community"],
    "market_information": ["Market Information Overview", "Mandi Prices", "Weather Forecasts", "Government Schemes", "Case Studies"],
    "media_resources": ["Media Hub", "Video Gallery", "Photo Gallery", "Events Calendar", "News & Updates", "Press Releases", "Media Contact", "Blogs & Articles", "Downloads"],
    "products": ["Products Master", "Formulations", "Intermediates", "Technicals", "Explore Brands"],
    "facilities": ["Manufacturing Excellence", "Overview of Facilities", "Manufacturing Facilities", "Research & Development", "Quality Control", "Future Scope"],
    "knowledge_centre": ["Knowledge Hub", "Expert Articles", "Video Library", "Training Materials", "FAQs on knowledge resources", "About the Knowledge Centre", "Contact for more info"],
    "about_us": ["Our Legacy", "Our Story", "Corporate Film", "Global Presence", "Leadership Team", "Meet the Management", "Awards & Recognitions", "News and Articles"],
    "investor_relations": ["Investor Hub", "Financials Overview", "Disclosures & Announcements", "Corporate Governance", "Stock Information"],
    "contact": ["Get in Touch", "Corporate Office", "Regional Offices", "Dealer Enquiry", "Customer Support", "Investor Contact"],
    "careers": ["Careers at Heranba", "Life at Heranba", "Why Heranba", "Open Positions", "Apply for a Job", "Employee Stories", "Contact HR"],
    
    # Sub-Pages
    "crop_advisory": ["Agricultural Advice", "Resources", "Expert Consultations"],
    "pest_diseases_guide": ["Management Strategies", "Identification", "Prevention"],
    "crop_calendars": ["Sowing Schedules", "Harvesting Periods"],
    "farmer_portal": ["Farmer Portal Dashboard", "Farmer Programs", "Farmer Testimonials", "Success Stories", "Contests", "Recognition Awards", "Heranba Farmer Community"],
    "mandi_prices": ["Mandi Price Insights", "Mandi Prices Updates", "Price Comparison", "Historical Trends"],
    "weather_forecasts": ["Weather Forecast Hub", "Daily Updates", "Weather Tips", "Seasonal Outlook"],
    "government_schemes": ["Govt Schemes List", "Available Schemes", "Assistance Programs", "Success Stories"],
    "case_studies": ["Case Studies Archive", "Project A", "Project B", "Analysis"],
    "formulations": ["Formulations Overview", "Crop Nutrition", "Fungicides", "Herbicides", "Insecticides", "Public Health"],
    "expert_articles": ["Expert Insights", "Featured", "Popular", "Contribute"],
    "video_library": ["Video Resources", "Categories", "Featured Videos", "Request Demo"],
    "training_materials": ["Learning Modules", "Course Intro", "Modules List"],
    "news_and_articles": ["News Archive", "Recent News", "Industry Articles", "Subscribe"],
    "management_team": ["Leadership Profiles", "Philosophy", "Profiles", "Structure"],
    "financials_overview": ["Financial Performance", "Annual Reports", "Quarterly Results", "Highlights"],
    "disclosures_announcements": ["Investor Disclosures", "Filings", "Press Releases", "Statutory"],
    "corporate_governance": ["Governance Framework", "Board", "Committees", "Policies", "Code"],
    "stock_information": ["Stock Market Data", "Price Chart", "Shareholding", "Dividends"],
    "contests": ["Farmer Contests", "Upcoming", "Past Winners", "Rules"],
    "recognition_awards": ["Award Recognition", "Categories", "Nomination", "Recipients"],
    "heranba_farmer_community": ["Community Forum", "Events", "Networking", "Join"],
    "crop_nutrition": ["Nutrition Solutions", "Bio Stimulant", "Bio Fertilizer", "Micro Nutrient Fertilizer", "Water Soluble Fertilizer", "PGR"],
    "fungicides": ["Fungicide Range", "Showcases", "Innovations", "Inquiry"],
    "herbicides": ["Herbicide Range", "Showcases", "Innovations", "Inquiry"],
    "insecticides": ["Insecticide Range", "Showcases", "Innovations", "Inquiry"],
    "public_health": ["Public Health Solutions", "Solutions", "Measures", "Learn"],
    "pgr": ["PGR Expert Guide", "About", "Products", "Benefits", "Usage", "FAQs", "Contact"],
    "water_soluble_fertilizer": ["WSF Products", "Intro", "Products", "Usage"],
    "micro_nutrient_fertilizer": ["Micro Nutrients", "Intro", "Products", "Usage"],
    "bio_fertilizer": ["Bio Solutions", "Intro", "Products", "Usage"],
    "bio_stimulant": ["Bio Stimulants", "Intro", "Products", "Usage"]
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

header_html = """<header><div class="logo-box">HERANBA</div><nav><a href="home.html">Home</a><a href="products.html">Products</a><a href="farmer_corner.html">Farmer Corner</a><a href="about_us.html">About</a><a href="contact.html">Contact</a></nav></header>"""
footer_html = """<footer><div class="footer-col"><h4>HERANBA</h4><ul><li>High-Quality Agrochemicals</li></ul></div><div class="footer-col"><h4>Navigation</h4><ul><li><a href="home.html" style="color:#fff;">Home</a></li><li>Products</li></ul></div><div class="footer-col"><h4>Legal</h4><ul><li>Privacy Policy</li><li>Terms</li></ul></div></footer>"""

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
