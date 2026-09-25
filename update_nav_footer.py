"""
update_nav_footer.py
Adds "Find Your Plan" to the nav and footer across all existing Speak.AI Marketing pages.
Run from the SpeakingMarketing project root directory.
"""
import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))

# All HTML files to update (relative to ROOT)
FILES = [
    "index.html",
    "about.html",
    "contact.html",
    "pricing.html",
    "services.html",
    "privacy.html",
    "services/ai-seo.html",
    "services/ai-content.html",
    "services/ai-social.html",
    "services/ai-ppc.html",
    "services/ai-email.html",
    "services/ai-analytics.html",
    "services/web-development.html",
]

# ── NAV: Insert "Find Your Plan" after the Pricing link ──────────────────────
NAV_FIND = '<a href="/find-your-plan" class="nav__link">Find Your Plan</a>'
NAV_AFTER = '<a href="/pricing"'          # insert AFTER the pricing link line
NAV_PATTERN = re.compile(
    r'(<a href="/pricing"[^>]*>Pricing</a>)',
    re.IGNORECASE
)

# ── FOOTER: Insert "Find Your Plan" between Pricing and Contact ───────────────
FOOTER_FIND = '<a href="/find-your-plan">Find Your Plan</a>\n'
FOOTER_AFTER_PATTERN = re.compile(
    r'(<a href="/pricing">Pricing</a>)',
    re.IGNORECASE
)

def process(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        src = f.read()

    changed = False

    # --- NAV ---
    if '/find-your-plan' not in src:
        if NAV_PATTERN.search(src):
            src = NAV_PATTERN.sub(r'\1\n                <a href="/find-your-plan" class="nav__link">Find Your Plan</a>', src)
            changed = True
    
    # --- FOOTER ---
    if 'find-your-plan' not in src or src.count('find-your-plan') < 2:
        if FOOTER_AFTER_PATTERN.search(src):
            src = FOOTER_AFTER_PATTERN.sub(
                r'\1\n                    <a href="/find-your-plan">Find Your Plan</a>',
                src,
                count=1  # only replace first footer occurrence (not the nav one already added)
            )
            changed = True

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(src)
        print("  [UPDATED] " + os.path.relpath(filepath, ROOT))
    else:
        print("  [SKIP]    " + os.path.relpath(filepath, ROOT))

if __name__ == '__main__':
    print("\nSpeak.AI Marketing — Nav & Footer Updater")
    print("==========================================")
    for rel in FILES:
        full = os.path.join(ROOT, rel)
        if os.path.exists(full):
            process(full)
        else:
            print("  [MISSING] " + rel)
    print("\nDone. Drag the updated files into GitHub to deploy.\n")
