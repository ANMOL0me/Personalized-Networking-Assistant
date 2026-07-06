# app/services/event_analyzer.py

KEYWORD_MAP = {
    "AI": ["ai", "artificial intelligence", "machine learning", "ml", "neural", "llm", "gpt"],
    "healthcare": ["health", "medical", "medicine", "hospital", "patient", "clinical"],
    "blockchain": ["blockchain", "crypto", "web3", "nft", "defi"],
    "education": ["education", "learning", "school", "university", "teach", "student"],
    "sustainability": ["sustainab", "climate", "green", "renewable", "environment"],
    "fintech": ["fintech", "finance", "payment", "banking", "investment"],
    "cybersecurity": ["cyber", "security", "hacking", "privacy", "encryption"],
    "biotech": ["biotech", "biology", "genom", "pharma", "life science"],
}


def extract_event_themes(description: str, candidate_labels=None):
    text = description.lower()
    scores = {}

    labels = candidate_labels or list(KEYWORD_MAP.keys())

    for label in labels:
        keywords = KEYWORD_MAP.get(label, [label.lower()])
        score = sum(text.count(kw) for kw in keywords)
        scores[label] = score

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top = [label for label, score in ranked if score > 0][:3]

    if not top:
        top = labels[:3]

    return top
