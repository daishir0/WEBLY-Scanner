from wcag_checker.utils import fetch_url, parse_html
import nltk
from nltk.corpus import wordnet

nltk.download('wordnet', quiet=True)

def check(url):
    html_content = fetch_url(url)
    if html_content is None:
        return False
    
    soup = parse_html(html_content)
    text = soup.get_text()
    words = text.split()
    
    ambiguous_words = []
    for word in words:
        synsets = wordnet.synsets(word)
        if len(synsets) > 1:
            ambiguous_words.append(word)
    
    if ambiguous_words:
        print(f"Potentially ambiguous words found: {', '.join(ambiguous_words)}")
        print("Manual check required: Verify if these words are ambiguous in the given context.")
        return False
    
    return True