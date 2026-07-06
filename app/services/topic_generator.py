# app/services/topic_generator.py

import random

TEMPLATES = [
    "What got you interested in {interest}, and how does it connect to {theme}?",
    "I've been following {theme} lately — have you seen any interesting overlap with {interest}?",
    "If you could combine {interest} with {theme}, what would you build first?",
    "What's the most surprising thing you've learned about {theme} recently?",
    "How do you see {interest} shaping the future of {theme}?",
    "What's a common misconception people have about {theme}?",
]


def generate_topics(event_themes, user_interests, count=3):
    themes = event_themes or ["this event"]
    interests = user_interests or ["your work"]

    suggestions = []
    used_templates = random.sample(TEMPLATES, min(count, len(TEMPLATES)))

    for i, template in enumerate(used_templates):
        theme = themes[i % len(themes)]
        interest = interests[i % len(interests)]
        suggestions.append(template.format(interest=interest, theme=theme))

    return suggestions
