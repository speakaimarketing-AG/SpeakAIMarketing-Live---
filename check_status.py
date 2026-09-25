import os

root = r'c:\Users\speak\OneDrive\Desktop\Office\SpeakingMarketing'

files = [
    'find-your-plan.html',
    'index.html', 'about.html', 'contact.html', 'pricing.html',
    'services.html', 'privacy.html',
    'services/ai-seo.html', 'services/ai-content.html',
    'services/ai-social.html', 'services/ai-ppc.html',
    'services/ai-email.html', 'services/ai-analytics.html',
    'services/web-development.html',
]

print('File status in local folder:')
print('-' * 60)
for f in files:
    path = os.path.join(root, f.replace('/', os.sep))
    if not os.path.exists(path):
        print('  MISSING  ' + f)
        continue
    content = open(path, encoding='utf-8').read()
    count = content.count('find-your-plan')
    if f == 'find-your-plan.html':
        print('  OK (new page)   ' + f)
    elif count >= 2:
        print('  OK (nav+footer) ' + f + '  [' + str(count) + ' refs]')
    elif count == 1:
        print('  PARTIAL (1 ref) ' + f)
    else:
        print('  MISSING LINK    ' + f)
