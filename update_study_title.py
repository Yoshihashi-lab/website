import re
import os

files = [
    '/Users/yu-macbookair/website/study.html',
    '/Users/yu-macbookair/website/en/study.html'
]

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Increase the main title font size (remove inline font-size or set it larger)
    # The user set .study-card-title { font-size: 1.8rem; } in style.css.
    # So we can remove the inline font-size from div.study-card-title
    content = re.sub(r'<div class="study-card-title" style="font-size: 1\.\d+rem;">', r'<div class="study-card-title">', content)
    
    # Increase the subtitle span font size to 1.3rem
    content = re.sub(r'style="font-size: 1rem; font-weight: normal; opacity: 0\.9;"', r'style="font-size: 1.3rem; font-weight: normal; opacity: 0.9;"', content)

    # Make sure Approach XX is also larger? Wait, Approach XX is in .study-card-number.
    # Let's check if .study-card-number needs font increase. Currently 0.72rem in style.css.
    # User said "Approach 01 ... この辺も大きくしたいです" so I should increase .study-card-number in style.css.

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# Update style.css to increase .study-card-number
css_file = '/Users/yu-macbookair/website/static/css/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(r'(\.study-card-number\s*\{[^}]*font-size:\s*)0\.72rem', r'\g<1>1rem', css)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated study.html, en/study.html, and style.css")
