import urllib.request
import re

urls = [
    'https://www.instagram.com/p/DUtRYeGDdzn/',
    'https://www.instagram.com/p/DUujyLFj8Tq/',
    'https://www.instagram.com/p/DVBleapAIx7/',
    'https://www.instagram.com/p/DVReY-flDno/',
    'https://www.instagram.com/p/DVS5dAWilxL/'
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
        html = urllib.request.urlopen(req).read().decode('utf-8')
        
        title_match = re.search(r'<title>(.*?)</title>', html)
        title = title_match.group(1) if title_match else 'Title not found'
        
        print(f'URL: {url}')
        print(f'Title: {title[:100]}')
        print('---')
    except Exception as e:
        print(f'Failed {url}: {e}')
