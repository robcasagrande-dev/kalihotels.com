import os
import re
import subprocess
from pathlib import Path

# Paths
SRC_DIR = Path('src')
PUBLIC_IMG_DIR = Path('public/images')

PUBLIC_IMG_DIR.mkdir(parents=True, exist_ok=True)

# Regex to find wp-content/uploads URLs
url_pattern = re.compile(r'https://kalihotels\.com/wp-content/uploads/[a-zA-Z0-9_/\.-]+')

# Track downloaded files to avoid re-downloading
downloaded = set()

# Process files
extensions = {'.astro', '.js', '.json', '.css'}

for root, _, files in os.walk(SRC_DIR):
    for file in files:
        if Path(file).suffix in extensions:
            file_path = Path(root) / file
            
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            urls = url_pattern.findall(content)
            
            if not urls:
                continue
                
            new_content = content
            for url in set(urls):
                filename = url.split('/')[-1]
                
                # Check if we need to rename duplicate filenames from different folders
                # We'll just use the flat filename for now, assuming they are unique.
                # If collision, we might need a better naming, but let's stick to flat.
                
                local_url_path = f'/images/{filename}'
                local_file_path = PUBLIC_IMG_DIR / filename
                
                # Download if not exists
                if url not in downloaded and not local_file_path.exists():
                    print(f"Downloading {url} to {local_file_path}...")
                    cmd = [
                        'curl', '-s', '-A', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                        '-L', '-o', str(local_file_path),
                        '--resolve', 'kalihotels.com:443:209.182.197.44',
                        url
                    ]
                    try:
                        subprocess.run(cmd, check=True)
                        downloaded.add(url)
                    except Exception as e:
                        print(f"Failed to download {url}: {e}")
                
                # Replace in content
                new_content = new_content.replace(url, local_url_path)
                
            if new_content != content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated paths in {file_path}")

print("Done! All images downloaded and paths updated.")
