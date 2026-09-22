import os

count = 0
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original = content
            content = content.replace('<script src="https://unpkg.com/@phosphor-icons/web@2.1.1"></script>', '<script defer src="https://unpkg.com/@phosphor-icons/web@2.1.1"></script>')
            
            if original != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1

print(f"Deferred Phosphor icons in {count} HTML files.")
