# Web Scraping for CTF - Extract Plain Text HTML from URLs

import requests
from bs4 import BeautifulSoup
import re

# ============================================
# 1. Simple URL Request & Text Extraction
# ============================================
def fetch_url_text(url):
    """Fetch HTML and return plain text"""
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

# Example usage
url = "https://example.com"
html_content = fetch_url_text(url)
if html_content:
    print("HTML content fetched successfully!")

# ============================================
# 2. Loop Through Multiple URLs
# ============================================
def scrape_multiple_urls(urls):
    """Loop through list of URLs and extract text"""
    for idx, url in enumerate(urls, 1):
        print(f"\n[{idx}] Fetching: {url}")
        html = fetch_url_text(url)
        if html:
            # Extract plain text (remove HTML tags)
            soup = BeautifulSoup(html, 'html.parser')
            plain_text = soup.get_text()
            print(f"Content length: {len(plain_text)} characters")

# Example
# urls = ["https://example.com", "https://example2.com"]
# scrape_multiple_urls(urls)

# ============================================
# 3. Extract Specific Patterns (CTF Flags)
# ============================================
def find_flags_in_html(url, pattern=r"flag{.*?}"):
    """Extract flag patterns from HTML"""
    html = fetch_url_text(url)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text()
        
        # Find all matches of the pattern
        flags = re.findall(pattern, text)
        return flags
    return []

# Example
# url = "https://ctf-challenge.com"
# flags = find_flags_in_html(url)
# print(f"Found flags: {flags}")

# ============================================
# 4. Loop & Extract Comments from HTML
# ============================================
def extract_html_comments(url):
    """Extract HTML comments (often contain hints in CTF)"""
    html = fetch_url_text(url)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        comments = soup.find_all(string=lambda text: isinstance(text, str) and text.strip().startswith('<!--'))
        
        for idx, comment in enumerate(comments, 1):
            print(f"\n[Comment {idx}]")
            print(comment)

# ============================================
# 5. Loop Through Form Inputs (CTF Recon)
# ============================================
def extract_forms(url):
    """Extract all forms from a page"""
    html = fetch_url_text(url)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        forms = soup.find_all('form')
        
        for idx, form in enumerate(forms, 1):
            print(f"\n[Form {idx}]")
            print(f"Action: {form.get('action')}")
            print(f"Method: {form.get('method')}")
            
            # Get all input fields
            inputs = form.find_all('input')
            for inp in inputs:
                print(f"  - {inp.get('name')}: {inp.get('type', 'text')}")

# ============================================
# 6. Loop Through All Links in Page
# ============================================
def extract_all_links(url):
    """Extract all links from a page"""
    html = fetch_url_text(url)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all('a')
        
        for idx, link in enumerate(links, 1):
            href = link.get('href', 'No href')
            text = link.get_text(strip=True) or 'No text'
            print(f"[{idx}] {text} -> {href}")

# ============================================
# 7. Extract Specific Tags in Loop
# ============================================
def extract_custom_tags(url, tag='script'):
    """Extract specific HTML tags (e.g., script, style)"""
    html = fetch_url_text(url)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        elements = soup.find_all(tag)
        
        print(f"Found {len(elements)} <{tag}> tags:\n")
        for idx, elem in enumerate(elements, 1):
            content = elem.get_text()[:100]  # First 100 chars
            print(f"[{idx}] {content}...")

# ============================================
# 8. Request with Headers & Loop Attempts
# ============================================
def scrape_with_retry(url, max_attempts=3):
    """Try fetching URL multiple times with headers"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    for attempt in range(1, max_attempts + 1):
        try:
            response = requests.get(url, headers=headers, timeout=5)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup.get_text()
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt}/{max_attempts} failed: {e}")
            if attempt == max_attempts:
                return None

# ============================================
# Note: Install required packages first:
# pip install requests beautifulsoup4
# ============================================
