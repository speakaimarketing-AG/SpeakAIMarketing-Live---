"""
update_nav_footer.py
Adds "Packages" footer column and fixes og:url tags across all existing pages.
"""
import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))

FILES = [
    "index.html",
    "about.html",
    "contact.html",
    "pricing.html",
    "services.html",
    "privacy.html",
    "find-your-plan.html",
    "services/ai-seo.html",
    "services/ai-content.html",
    "services/ai-social.html",
    "services/ai-ppc.html",
    "services/ai-email.html",
    "services/ai-analytics.html",
    "services/web-development.html",
]

PACKAGES_COL = """                <div class="footer__col">
                    <h4 class="footer__heading">Packages</h4>
                    <a href="/packages/focus">Focus</a>
                    <a href="/packages/traffic-accelerator">Traffic Accelerator</a>
                    <a href="/packages/growth-system">Growth System</a>
                    <a href="/packages/website-launch">Website Launch</a>
                    <a href="/packages/website-care">Website Care &amp; GBP</a>
                </div>"""

def process(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        src = f.read()

    changed = False

    # 1. Clean og:url tags (.html -> clean URL)
    og_pattern = re.compile(r'content="https://speakaimarketing\.com/([^"]+)\.html"')
    if og_pattern.search(src):
        src = og_pattern.sub(r'content="https://speakaimarketing.com/\1"', src)
        changed = True

    # 2. Add Packages column in footer if missing
    if '/packages/focus' not in src:
        # Insert before Company column
        company_pattern = re.compile(r'(\s*<div class="footer__col">\s*<h4 class="footer__heading">Company</h4>)', re.IGNORECASE)
        if company_pattern.search(src):
            src = company_pattern.sub('\n' + PACKAGES_COL + r'\1', src, count=1)
            changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(src)
        print("  [UPDATED] " + os.path.relpath(filepath, ROOT))
    else:
        print("  [SKIP]    " + os.path.relpath(filepath, ROOT))

if __name__ == '__main__':
    print("\nSpeak.AI Marketing — Site SEO & Footer Updater")
    print("==============================================")
    for rel in FILES:
        full = os.path.join(ROOT, rel.replace('/', os.sep))
        if os.path.exists(full):
            process(full)
        else:
            print("  [MISSING] " + rel)
    print("\nDone.\n")
