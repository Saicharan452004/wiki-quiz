import requests
import re
from bs4 import BeautifulSoup


def clean_text(value: str) -> str:
    value = re.sub(r"\[\d+\]", "", value)   # remove [1], [23], etc.
    value = re.sub(r"\s+", " ", value)      # fix spacing issues
    return value.strip()


def scrape_wikipedia(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (WikiQuizApp/1.0)"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Title
    title = soup.find("h1").get_text(strip=True)

    # Summary (first non-empty paragraph)
    summary = ""
    for p in soup.select("#mw-content-text p"):
        text = p.get_text(strip=True)
        if text:
            summary = clean_text(text)
            break

    # Sections
    sections = [
        h.get_text(strip=True)
        for h in soup.select("#mw-content-text h2")
    ]

    # Full article text
    paragraphs = soup.select("#mw-content-text p")
    full_text = " ".join(p.get_text(strip=True) for p in paragraphs)
    full_text = clean_text(full_text)[:12000]


    return {
        "title": title,
        "summary": summary,
        "sections": sections,
        "text": full_text
    }
