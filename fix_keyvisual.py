import re

css_file = '/Users/yu-macbookair/website/static/css/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# Update .keyvisual to have max-width and margin auto
css = re.sub(
    r'(\.keyvisual\s*\{[^}]*width:\s*100%;)', 
    r'\1\n  max-width: var(--max-width);\n  margin: 0 auto;\n  border-radius: var(--radius-lg);', 
    css
)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css")
