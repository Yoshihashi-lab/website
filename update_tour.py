import re

def update_tour(filepath, is_en=False):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update font sizes
    # Title
    content = re.sub(r'(#title\s*\{[^}]*font-size:\s*)14px', r'\g<1>22px', content)
    
    # City label font sizes
    if is_en:
        content = re.sub(r'(\.city-label\s*\{[^}]*font-size:\s*)10px', r'\g<1>15px', content)
        content = re.sub(r'(\.city\.active\s*\.city-label\s*\{[^}]*font-size:\s*)11px', r'\g<1>17px', content)
    else:
        content = re.sub(r'(\.city-label\s*\{[^}]*font-size:\s*)13px', r'\g<1>16px; font-weight: bold', content)
        content = re.sub(r'(\.city\.active\s*\.city-label\s*\{[^}]*font-size:\s*)15px', r'\g<1>18px', content)

    # 2. Update aspect ratio and dimensions
    if is_en:
        # Convert fixed width/height to responsive aspect ratio
        content = re.sub(r'width:\s*880px;', 'width: 100%;\n            max-width: 1120px;', content)
        content = re.sub(r'height:\s*500px;', 'aspect-ratio: 1120 / 630;', content)
        content = re.sub(r'viewBox="0 0 880 500"', 'viewBox="0 0 1120 630"', content)
        content = re.sub(r'width="880" height="500"', 'width="1120" height="630"', content)
        content = re.sub(r'translate\(835, 45\)', 'translate(1060, 55)', content)
        content = re.sub(r'y="480"', 'y="600"', content)
        content = re.sub(r'fitExtent\(\[\[40, 40\], \[840, 460\]\]', 'fitExtent([[20, 20], [1100, 610]]', content)
        
        # Update js coordinates to use percentages
        content = re.sub(r'wrap\.style\.left = c\.x \+ \'px\';', 'wrap.style.left = (c.x / 1120 * 100) + \'%\';', content)
        content = re.sub(r'wrap\.style\.top = c\.y \+ \'px\';', 'wrap.style.top = (c.y / 630 * 100) + \'%\';', content)
        content = re.sub(r'avatar\.style\.left = initCity\.x \+ \'px\';', 'avatar.style.left = (initCity.x / 1120 * 100) + \'%\';', content)
        content = re.sub(r'avatar\.style\.top = initCity\.y \+ \'px\';', 'avatar.style.top = (initCity.y / 630 * 100) + \'%\';', content)
        content = re.sub(r'avatar\.style\.left = toCity\.x \+ \'px\';', 'avatar.style.left = (toCity.x / 1120 * 100) + \'%\';', content)
        content = re.sub(r'avatar\.style\.top = toCity\.y \+ \'px\';', 'avatar.style.top = (toCity.y / 630 * 100) + \'%\';', content)
        content = re.sub(r'bubble\.style\.left = Math\.max\(80, Math\.min\(800, x\)\) \+ \'px\';', 'bubble.style.left = (Math.max(80, Math.min(1040, x)) / 1120 * 100) + \'%\';', content)
        content = re.sub(r'bubble\.style\.top = \(y - 65\) \+ \'px\';', 'bubble.style.top = ((y - 65) / 630 * 100) + \'%\';', content)
        content = re.sub(r'left:\$\{x\}px; top:\$\{y\}px;', 'left:${x / 1120 * 100}%; top:${y / 630 * 100}%;', content)
    else:
        # Update aspect ratio in JP
        content = re.sub(r'aspect-ratio: 1120 / 1060;', 'aspect-ratio: 1120 / 630;', content)
        content = re.sub(r'viewBox="0 0 1120 1060"', 'viewBox="0 0 1120 630"', content)
        content = re.sub(r'width="1120" height="1060"', 'width="1120" height="630"', content)
        content = re.sub(r'y="1030"', 'y="600"', content)
        content = re.sub(r'font-size="12"', 'font-size="16"', content) # SVG text font size
        content = re.sub(r'fitExtent\(\[\[20, 20\], \[1100, 1040\]\]', 'fitExtent([[20, 20], [1100, 610]]', content)
        
        # Update js percentage math
        content = re.sub(r'/ 1060 \* 100', '/ 630 * 100', content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

update_tour("/Users/yu-macbookair/website/tour.html", False)
update_tour("/Users/yu-macbookair/website/en/tour.html", True)

# Update index files
def update_index(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace("aspect-ratio: 1120 / 1060;", "aspect-ratio: 1120 / 630;")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

update_index("/Users/yu-macbookair/website/index.html")
update_index("/Users/yu-macbookair/website/en/index.html")

print("Updates applied")
