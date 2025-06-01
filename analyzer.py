import requests
from bs4 import BeautifulSoup
import textstat
import os

def fetch_article_text(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for script in soup(["script", "style"]):
            script.extract()
        return soup.get_text(separator=' ', strip=True)
    else:
        raise Exception(f"Failed to fetch URL: {url} (Status: {response.status_code})")

def assess_readability(text):
    score = textstat.flesch_reading_ease(text)
    suggestions = []
    if score < 60:
        suggestions.append("The article is moderately hard to read. Simplify complex words and shorten long sentences.")
    else:
        suggestions.append("The article is easy to read for non-technical marketers.")
    return {
        "score": score,
        "assessment": f"Flesch Reading Ease: {score}.",
        "suggestions": suggestions
    }

def analyze_structure(text):
    lines = text.split('\n')
    long_paragraphs = [line for line in lines if len(line.split()) > 100]
    suggestions = []
    if long_paragraphs:
        suggestions.append(f"Found {len(long_paragraphs)} overly long paragraphs. Break them into shorter chunks.")
    return {
        "assessment": "Checked paragraph length and flow.",
        "suggestions": suggestions
    }

def assess_completeness(text):
    suggestions = []
    if "example" not in text.lower():
        suggestions.append("No examples found. Consider adding examples for better understanding.")
    return {
        "assessment": "Checked for completeness and examples.",
        "suggestions": suggestions
    }

def check_style_guidelines(text):
    suggestions = []
    if any(word in text.lower() for word in ["leverage", "utilize", "paradigm"]):
        suggestions.append("Replace jargon like 'leverage' or 'utilize' with simpler words like 'use'.")
    if any(len(sent.split()) > 25 for sent in text.split('.')):
        suggestions.append("Some sentences are too long. Consider breaking them into shorter ones.")
    return {
        "assessment": "Checked tone, jargon, and sentence length.",
        "suggestions": suggestions
    }

def generate_report(url, text, output_path="report_output/result1.md"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    readability = assess_readability(text)
    structure = analyze_structure(text)
    completeness = assess_completeness(text)
    style = check_style_guidelines(text)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"#  Documentation Analysis Report\n\n")
        f.write(f"**URL Analyzed:** {url}\n\n")
        
        f.write("##  1. Readability for a Marketer\n")
        f.write(f"- Assessment: {readability['assessment']}\n")
        for s in readability["suggestions"]:
            f.write(f"- Suggestion: {s}\n")

        f.write("\n##  2. Structure and Flow\n")
        f.write(f"- Assessment: {structure['assessment']}\n")
        for s in structure["suggestions"]:
            f.write(f"- Suggestion: {s}\n")

        f.write("\n##  3. Completeness of Information & Examples\n")
        f.write(f"- Assessment: {completeness['assessment']}\n")
        for s in completeness["suggestions"]:
            f.write(f"- Suggestion: {s}\n")

        f.write("\n##  4. Adherence to Style Guidelines\n")
        f.write(f"- Assessment: {style['assessment']}\n")
        for s in style["suggestions"]:
            f.write(f"- Suggestion: {s}\n")
