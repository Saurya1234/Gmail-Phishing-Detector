import re
from urllib.parse import urlparse

KEYWORDS = [
    "urgent",
    "verify",
    "suspended",
    "login now",
    "click here",
    "password reset",
    "bank alert"
]

def extract_urls(text):
    return re.findall(r'https?://[^\s]+', text)

def suspicious_url(url):
    parsed = urlparse(url)

    if parsed.hostname:
        if re.match(r"\d+\.\d+\.\d+\.\d+", parsed.hostname):
            return True

        if parsed.hostname.endswith((".xyz", ".top", ".tk")):
            return True

    return False

def scan_email(body):
    score = 0
    reasons = []

    for word in KEYWORDS:
        if word in body.lower():
            score += 10
            reasons.append(f"Keyword: {word}")

    for url in extract_urls(body):
        if suspicious_url(url):
            score += 30
            reasons.append(f"Suspicious URL: {url}")

    status = "safe"

    if score >= 60:
        status = "malicious"
    elif score >= 40:
        status = "suspicious"

    return {
        "score": score,
        "status": status,
        "reasons": reasons
    }