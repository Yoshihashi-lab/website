import re

# 1. Fix style.css for .keyvisual
css_file = '/Users/yu-macbookair/website/static/css/style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(
    r'\.keyvisual\s*\{[^}]*\}',
    '''.keyvisual {
  width: 100%;
  max-height: 460px;
  overflow: hidden;
  position: relative;
  background-color: var(--color-primary);
}''',
    css
)

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css)


# 2. Fix study.html .slogan-section
study_jp = '/Users/yu-macbookair/website/study.html'
with open(study_jp, 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(
    r'style="position: relative; margin: 40px 0 60px; padding: 20px; border-radius: 16px; box-shadow: 0 10px 30px rgba\(0, 0, 0, 0\.3\); background-image: url\(\'static/img/neutron_bg\.png\'\); background-size: cover; background-position: center; background-repeat: no-repeat; overflow: hidden; aspect-ratio: 16 / 9;"',
    'style="position: relative; width: 100vw; left: 50%; right: 50%; margin-left: -50vw; margin-right: -50vw; margin-top: 0; margin-bottom: 60px; padding: 20px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3); background-image: url(\'static/img/neutron_bg.png\'); background-size: cover; background-position: center; background-repeat: no-repeat; overflow: hidden; aspect-ratio: 16 / 9;"',
    content
)

# Also check for neutron_application.jpg if the user hasn't saved the switch to neutron_bg.png yet
content = re.sub(
    r'style="position: relative; margin: 40px 0 60px; padding: 20px; border-radius: 16px; box-shadow: 0 10px 30px rgba\(0, 0, 0, 0\.3\); background-image: url\(\'static/img/neutron_application\.jpg\'\); background-size: cover; background-position: center; background-repeat: no-repeat; overflow: hidden; aspect-ratio: 16 / 9;"',
    'style="position: relative; width: 100vw; left: 50%; right: 50%; margin-left: -50vw; margin-right: -50vw; margin-top: 0; margin-bottom: 60px; padding: 20px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3); background-image: url(\'static/img/neutron_application.jpg\'); background-size: cover; background-position: center; background-repeat: no-repeat; overflow: hidden; aspect-ratio: 16 / 9;"',
    content
)

with open(study_jp, 'w', encoding='utf-8') as f:
    f.write(content)


# 3. Fix en/study.html .slogan-section
study_en = '/Users/yu-macbookair/website/en/study.html'
with open(study_en, 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(
    r'style="position: relative; margin: 40px 0 60px; padding: 20px; border-radius: 16px; box-shadow: 0 10px 30px rgba\(0, 0, 0, 0\.3\); background-image: url\(\'\.\./static/img/neutron_bg\.png\'\); background-size: cover; background-position: center; background-repeat: no-repeat; overflow: hidden; aspect-ratio: 16 / 9;"',
    'style="position: relative; width: 100vw; left: 50%; right: 50%; margin-left: -50vw; margin-right: -50vw; margin-top: 0; margin-bottom: 60px; padding: 20px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3); background-image: url(\'../static/img/neutron_bg.png\'); background-size: cover; background-position: center; background-repeat: no-repeat; overflow: hidden; aspect-ratio: 16 / 9;"',
    content
)

# And fallback for application
content = re.sub(
    r'style="position: relative; margin: 40px 0 60px; padding: 20px; border-radius: 16px; box-shadow: 0 10px 30px rgba\(0, 0, 0, 0\.3\); background-image: url\(\'\.\./static/img/neutron_application\.jpg\'\); background-size: cover; background-position: center; background-repeat: no-repeat; overflow: hidden; aspect-ratio: 16 / 9;"',
    'style="position: relative; width: 100vw; left: 50%; right: 50%; margin-left: -50vw; margin-right: -50vw; margin-top: 0; margin-bottom: 60px; padding: 20px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3); background-image: url(\'../static/img/neutron_application.jpg\'); background-size: cover; background-position: center; background-repeat: no-repeat; overflow: hidden; aspect-ratio: 16 / 9;"',
    content
)

with open(study_en, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updates applied to style.css, study.html, and en/study.html")
